import errno
import json
import os
import random
from typing import Union

import matplotlib.pyplot as plt
import numpy as np
from elasticsearch import NotFoundError

from oss.db.bulk import KNNBulkOperations, KNNBulkRelationship
from oss.db.models import (
    Dataset,
    ElasticSearchIndex,
    EmbeddingSpace,
    Experiment,
    create_tables,
)
from oss.es.api import Mapping, NearestNeighborsQuery, Similarity, Vec
from oss.es.client import ElastiKNNClient
from oss.es.utils import load_csv_with_headers, load_embeddings_from_numpy
from oss.oss.exceptions import (
    CreatingIndexError,
    DimensionsDismatchError,
    IDFieldNotUnique,
    IsNotAColumnError,
    OperationNotAllowedError,
    RecursiveOperationNotAllowedError,
)
from oss.oss.utils import edit_es_indices


def add_dataset(
    name: str,
    csv_path: str,
    id_field: str = "_idx",
):
    create_tables()

    csv_abs_path = os.path.abspath(csv_path)

    if not os.path.isfile(csv_abs_path):
        raise FileNotFoundError(f"Could not find file {csv_abs_path}")

    if id_field is None:
        id_field = "_idx"
    rows, _, header = load_csv_with_headers(csv_abs_path, id_field)
    ids = []
    for row in rows:
        ids.append(row[id_field])
    if len(ids) != len(set(ids)):
        raise IDFieldNotUnique("Error: the id field column must have unique values")

    dataset = Dataset.create(name=name, csv_path=csv_abs_path, id_field=id_field)

    return dataset


def add_experiment(
    name: str,
    train_dataset_name: str,
    model_name: str,
    params: Union[dict, str] = {},
    params_path: str = None,
):
    try:
        train_dataset = Dataset.get(name=train_dataset_name)
    except Dataset.DoesNotExist:
        raise Dataset.DoesNotExist(f"{train_dataset_name} is not a Dataset")

    if params != {} and params_path is not None:
        raise TypeError("Only one of 'params' and 'param_path' should be given")

    if params_path is not None:
        params_absolute_path = os.path.abspath(params_path)
        if not os.path.isfile(params_absolute_path):
            raise FileNotFoundError(f"Could not find file {params_absolute_path}")
        with open("strings.json") as f:
            params_json = json.load(f)
    else:
        params_json = json.dumps(params)

    experiment = Experiment.create(
        name=name, model=model_name, train_dataset=train_dataset, params=params_json
    )

    return experiment


def add_embedding_space(
    name: str,
    npz_path: str,
    dims: int,
    experiment_name: str,
    dataset_name: str,
):
    try:
        experiment = Experiment.get(name=experiment_name)
    except Experiment.DoesNotExist:
        raise Experiment.DoesNotExist(f"{experiment_name} is not an Experiment")

    try:
        dataset = Dataset.get(name=dataset_name)
    except Dataset.DoesNotExist:
        raise Dataset.DoesNotExist(f"{dataset_name} is not a Dataset")

    npz_abs_path = os.path.abspath(npz_path)
    if not os.path.isfile(npz_abs_path):
        raise FileNotFoundError(f"Could not find file {npz_abs_path}")

    embeddings = load_embeddings_from_numpy(npz_abs_path)
    if embeddings.shape[1] != dims:
        raise ValueError("The given dimensions doesn't match npz dimensions")

    embedding_space = EmbeddingSpace.create(
        name=name,
        npz_path=npz_abs_path,
        dims=dims,
        experiment=experiment,
        dataset=dataset,
    )

    return embedding_space


def get_datasets(
    name: str = None,
    csv_path: str = None,
    id_field: str = None,
):
    if csv_path is not None:
        csv_path = os.path.abspath(csv_path)

    condition = {"name": name, "csv_path": csv_path, "id_field": id_field}
    condition = {k: v for k, v in condition.items() if v is not None}
    query = Dataset.select()
    for column, value in condition.items():
        query = query.where(getattr(Dataset, column) == value)

    return [result for result in query]


def get_experiments(
    name: str = None,
    train_dataset: str = None,
    model: str = None,
    params: Union[dict, str] = None,
):
    if train_dataset is not None:
        try:
            train_dataset = Dataset.get(name=train_dataset)
        except Dataset.DoesNotExist:
            raise ValueError(f"{train_dataset} is not a Dataset")

    condition = {
        "name": name,
        "train_dataset": train_dataset,
        "model": model,
        "params": params,
    }
    condition = {k: v for k, v in condition.items() if v is not None}
    query = Experiment.select()
    for column, value in condition.items():
        query = query.where(getattr(Experiment, column) == value)

    return [result for result in query]


def get_embedding_spaces(
    name: str = None,
    experiment: str = None,
    dataset: str = None,
    npz_path: str = None,
    dims: int = None,
):

    if experiment is not None:
        try:
            experiment = Experiment.get(name=experiment)
        except Experiment.DoesNotExist:
            raise ValueError(f"{experiment} is not an Experiment")

    if dataset is not None:
        try:
            dataset = Dataset.get(name=dataset)
        except Dataset.DoesNotExist:
            raise ValueError(f"{dataset} is not a Dataset")

    if npz_path is not None:
        npz_path = os.path.abspath(npz_path)

    condition = {
        "name": name,
        "experiment": experiment,
        "dataset": dataset,
        "npz_path": npz_path,
        "dims": dims,
    }
    condition = {k: v for k, v in condition.items() if v is not None}
    query = EmbeddingSpace.select()
    for column, value in condition.items():
        query = query.where(getattr(EmbeddingSpace, column) == value)

    return [result for result in query]


def delete_dataset(
    name: str,
    allow_recursive: bool = False,
    delete_indices: bool = False,
):
    try:
        dataset = Dataset.get(name=name)
    except Dataset.DoesNotExist:
        raise ValueError(f"{name} is not a Dataset")

    embedding_spaces = []
    experiments = Experiment.select().where(Experiment.train_dataset == dataset)
    for exp in experiments:
        emb_spaces = EmbeddingSpace.select().where(EmbeddingSpace.experiment == exp)
        for emb_space in emb_spaces:
            if emb_space not in embedding_spaces:
                embedding_spaces.append(emb_space)

    for emb_space in EmbeddingSpace.select().where(EmbeddingSpace.dataset == dataset):
        if emb_space not in embedding_spaces:
            embedding_spaces.append(emb_space)

    if (len(experiments) != 0) and (len(embedding_spaces) != 0) and not allow_recursive:
        raise RecursiveOperationNotAllowedError

    indices = []
    for emb_space in embedding_spaces:
        inds = ElasticSearchIndex.select().where(
            ElasticSearchIndex.embedding_space == emb_space
        )
        for index in inds:
            if index not in indices:
                indices.append(index)

    if (len(indices) == 0) or delete_indices:
        es = ElastiKNNClient()
        for index in indices:
            es.delete_index(index.name)
        es.close()
        return dataset.delete_instance(recursive=True)
    else:
        raise RecursiveOperationNotAllowedError


def delete_experiment(
    name: str,
    delete_indices: bool = False,
    allow_recursive: bool = False,
):
    try:
        experiment = Experiment.get(name=name)
    except Experiment.DoesNotExist:
        raise ValueError(f"{name} is not an Experiment")
    embedding_spaces = EmbeddingSpace.select().where(
        EmbeddingSpace.experiment == experiment
    )
    indices = []
    for embedding_space in embedding_spaces:
        inds = ElasticSearchIndex.select().where(
            ElasticSearchIndex.embedding_space == embedding_space
        )
        for index in inds:
            if index not in indices:
                indices.append(index)

    if (len(embedding_spaces) != 0) and not allow_recursive:
        raise RecursiveOperationNotAllowedError

    if (len(indices) == 0) or delete_indices:
        es = ElastiKNNClient()
        for index in indices:
            es.delete_index(index.name)
        es.close()
        return experiment.delete_instance(recursive=True, delete_nullable=False)
    else:
        raise RecursiveOperationNotAllowedError


def delete_embedding_space(
    name: str,
    delete_indices: bool = False,
    allow_recursive: bool = False,
):
    try:
        embedding_space = EmbeddingSpace.get(name=name)
    except EmbeddingSpace.DoesNotExist:
        raise ValueError(f"{name} is not an Embedding space")

    indices = [
        index
        for index in ElasticSearchIndex.select().where(
            ElasticSearchIndex.embedding_space == embedding_space
        )
    ]

    if (len(indices) == 0) or delete_indices:
        es = ElastiKNNClient()
        for index in indices:
            es.delete_index(index.name)
        es.close()
        return embedding_space.delete_instance(recursive=True, delete_nullable=False)
    else:
        raise RecursiveOperationNotAllowedError


def edit_dataset(
    name, column, new_value, edit_indices: bool = False, allow_recursive: bool = False
):
    try:
        dataset = Dataset.get(name=name)
    except Dataset.DoesNotExist:
        raise ValueError(f"Error: {name} is not a dataset")

    if column not in ["name", "csv-path", "id-field"]:
        raise ValueError(
            f"Unknown column {column} for {object}, try one of:\n "
            f"- name\n - csv-path\n - id-field"
        )

    embedding_spaces = []
    experiments = Experiment.select().where(Experiment.train_dataset == dataset)
    for exp in experiments:
        emb_spaces = EmbeddingSpace.select().where(EmbeddingSpace.experiment == exp)
        for emb_space in emb_spaces:
            if emb_space not in embedding_spaces:
                embedding_spaces.append(emb_space)

    for emb_space in EmbeddingSpace.select().where(EmbeddingSpace.dataset == dataset):
        if emb_space not in embedding_spaces:
            embedding_spaces.append(emb_space)

    if (len(experiments) != 0) and (len(embedding_spaces) != 0) and not allow_recursive:
        raise RecursiveOperationNotAllowedError(
            "Editing this dataset will edit all the "
            + "experiments and embedding spaces generated from it. if this is what you "
            + "want, set allow_recursive True."
        )

    indices = []
    for emb_space in embedding_spaces:
        inds = ElasticSearchIndex.select().where(
            ElasticSearchIndex.embedding_space == emb_space
        )
        for index in inds:
            if index not in indices:
                indices.append(index)

    if column == "id_field":
        rows, _, header = load_csv_with_headers(dataset.csv_path)
        if new_value is None:
            new_value = "_idx"
        elif new_value not in header:
            raise ValueError(f"Error: {new_value} is not a column of the given csv")
        else:
            ids = []
            for row in rows:
                ids.append(row[new_value])
            if len(ids) != len(set(ids)):
                raise ValueError("Error: the id field column must have unique values")
        column = "id-field"

    elif column == "csv-path":
        rows, _, header = load_csv_with_headers(dataset.csv_path)
        new_value = os.path.abspath(new_value)
        if not os.path.isfile(new_value):
            raise FileNotFoundError(f"Could not find file {new_value}")
        ids = []
        for row in rows:
            ids.append(row[dataset.id_field])
        if len(ids) != len(set(ids)):
            raise ValueError("Error: the id field column must have unique values")
        column = "csv_path"

    if (len(indices) == 0) or edit_indices:
        return edit_es_indices(indices, dataset, column, new_value, Dataset)
    else:
        raise RecursiveOperationNotAllowedError(
            "This operation would re-index the following indices:",
            [index.name for index in indices],
        )


def edit_experiment(
    name,
    column,
    new_value,
    allow_recursive: bool = True,
):
    try:
        experiment = Experiment.get(name=name)
    except Experiment.DoesNotExist:
        raise ValueError(f"Error: {name} is not an experiment")

    if column not in ["name", "train_dataset", "model", "parameters"]:
        raise ValueError(
            f"Unknown column {column} for {object}, try one of:\n "
            f"- name\n - dataset\n - model\n - parameters\n"
        )

    query_embedding_spaces = EmbeddingSpace.select().where(
        EmbeddingSpace.experiment == experiment
    )
    embedding_spaces = [embedding_space for embedding_space in query_embedding_spaces]

    indices = []
    for embedding_space in embedding_spaces:
        inds = ElasticSearchIndex.select().where(
            ElasticSearchIndex.embedding_space == embedding_space
        )
        for index in inds:
            if index not in indices:
                indices.append(index)

    if (len(embedding_spaces) != 0) and not allow_recursive:
        raise RecursiveOperationNotAllowedError(
            "Editing this experiment will edit all the "
            + "embedding spaces generated from it. if this is what you "
            + "want, set allow_recursive True."
        )

    else:
        if column == "train_dataset":
            try:
                new_value = Dataset.get(name=new_value)
            except Dataset.DoesNotExist:
                raise ValueError(f"Error: {new_value} is not a Dataset")
    return edit_es_indices([], experiment, column, new_value, Experiment)


def edit_embedding_space(name, column, new_value, edit_indices: bool = True):
    try:
        embedding_space = EmbeddingSpace.get(name=name)
    except EmbeddingSpace.DoesNotExist:
        raise ValueError(f"Error: {name} is not an embedding space")

    if column not in ["name", "experiment", "dataset", "npz-path", "dims"]:
        raise ValueError(
            f"Unknown column {column} for {object}, try one of:\n "
            f"- name\n - npz-path\n - dims\n - experiment\n - dataset\n"
        )

    if column == "dims":
        new_value = int(new_value)

    elif column == "npz-path":
        new_value = os.path.abspath(new_value)
        if not os.path.isfile(new_value):
            FileNotFoundError(f"Could not find file {new_value}")
        column = "npz_path"

    elif column == "experiment":
        try:
            new_value = Experiment.get(name=new_value)
        except Experiment.DoesNotExist:
            ValueError(f"Error: {new_value} is not a Experiment")

    elif column == "dataset":
        try:
            new_value = Dataset.get(name=new_value)
        except Dataset.DoesNotExist:
            raise ValueError(f"Error: {new_value} is not a Dataset")
    indices = [
        index
        for index in ElasticSearchIndex.select().where(
            ElasticSearchIndex.embedding_space == embedding_space
        )
    ]

    if (len(indices) == 0) or (edit_indices):
        return edit_es_indices(
            indices, embedding_space, column, new_value, EmbeddingSpace
        )

    else:
        raise RecursiveOperationNotAllowedError(
            "This operation would re-index the following indices:",
            [index.name for index in indices],
        )


def load_index(
    index_name,
    embedding_space_name,
    mapping: Mapping = None,
    num_threads: int = 4,
    chunk_size: int = 1000,
    number_of_shards: int = 1,
) -> int:

    es = ElastiKNNClient()

    if index_name in es.list_indices():
        es.close()
        raise ValueError(f"Error: {index_name} is already loaded")

    embedding_space = EmbeddingSpace.get(name=embedding_space_name)

    embeddings = load_embeddings_from_numpy(embedding_space.npz_path)
    rows, header_mapping, header = load_csv_with_headers(
        embedding_space.dataset.csv_path
    )

    if embeddings.shape[0] != len(rows):
        es.close()
        raise DimensionsDismatchError("csv and npz have different number of rows")
    if embeddings.shape[1] != embedding_space.dims:
        es.close()
        raise DimensionsDismatchError("embedding_space.dims does not match npz dims")

    if mapping is None:
        mapping = Mapping.CosineLsh(dims=embedding_space.dims, L=99, k=1)

    if isinstance(mapping, Mapping.CosineLsh):
        similarity = "cosine"
        model = "lsh"
        k = mapping.k
        L = mapping.L
        w = None
    elif isinstance(mapping, Mapping.L2Lsh):
        similarity = "l2"
        model = "lsh"
        k = mapping.k
        L = mapping.L
        w = mapping.w
    elif isinstance(mapping, Mapping.DenseFloat):
        similarity = None
        model = "exact"
        k = None
        L = None
        w = None
    else:
        es.close()
        raise ValueError("'Mapping' not suported")
    vecs = []
    for embedding in embeddings:
        vecs.append(Vec.DenseFloat(list(embedding)))

    if len(rows) != len(vecs):
        es.close()
        raise DimensionsDismatchError(
            "Error: number of rows in csv file doesn't match the number of embeddings"
            "in npz file"
        )

    response = es.create_index(
        index_name=index_name,
        mapping=mapping,
        header_mapping=header_mapping,
        number_of_shards=number_of_shards,
    )

    if not response["acknowledged"]:
        es.close()
        raise CreatingIndexError("An error occurred while creating the index.")

    try:
        successes = es.index(
            index=index_name,
            vecs=vecs,
            metadata=rows,
            id_field=embedding_space.dataset.id_field,
            num_threads=num_threads,
            chunk_size=chunk_size,
        )
    except OSError as e:
        if e.errno == errno.ENOSPC:
            delete_index(index_name=index_name)
            es.close()
            raise OSError("Not enough space in disk")
    es.close()

    assert successes == len(rows)
    try:
        ElasticSearchIndex.create(
            name=index_name,
            embedding_space=embedding_space,
            model=model,
            similarity=similarity,
            num_threads=num_threads,
            chunk_size=chunk_size,
            k=k,
            L=L,
            w=w,
            number_of_shards=number_of_shards,
        )
    except Exception as e:
        delete_index(index_name=index_name)
        es.close()
        raise e

    print("Index loaded")
    return successes


def delete_index(index_name: str):
    try:
        es_index = ElasticSearchIndex.get(name=index_name)
    except ElasticSearchIndex.DoesNotExist:
        raise ValueError(f"Error: `{index_name}` is not an index")

    es = ElastiKNNClient()

    if index_name not in es.list_indices():
        raise ValueError(f"Error: {index_name} is not an index")
    else:
        result = es.delete_index(index_name=index_name)
        es_index.delete_instance(recursive=True, delete_nullable=False)

    es.close()

    return result


def list_indices():
    es = ElastiKNNClient()
    indices = es.list_indices()
    es.close()

    return indices


def match_query(
    indices_name: list[str],
    query_id: str = None,
    random_query: bool = False,
    k: int = 10,
    fetch_source: bool = False,
):
    if (query_id is None) and (not random_query):
        raise ValueError("Either 'query_id' or 'random_query' must be given.")

    # Check if all indices have the same dataset
    dataset = ElasticSearchIndex.get(name=indices_name[0]).embedding_space.dataset

    for index_name in indices_name:
        try:
            index = ElasticSearchIndex.get(name=index_name)
        except ElasticSearchIndex.DoesNotExist:
            raise ValueError(f"{index_name} is not an index")

        if index.embedding_space.dataset.name != dataset.name:
            raise ValueError(  # CHANGE
                f"Error: All indices must have the same dataset, but index "
                f"{index_name} has dataset {index.embedding_space.dataset.name} "
                f"and index {indices_name[0]} has dataset {dataset.name}"
            )
    es = ElastiKNNClient()

    if random_query:
        rows, _, header = load_csv_with_headers(dataset.csv_path)  # type: ignore
        query_id = random.choice(rows)[dataset.id_field]

    results = {}
    print(f"Querying: {dataset.id_field} = {query_id}")
    for index_name in indices_name:
        try:

            index = ElasticSearchIndex.get(name=index_name)
            query_vec = Vec.Indexed(index=index_name, id=query_id)
            if index.model == "lsh":
                if index.similarity == "cosine":
                    query = NearestNeighborsQuery.CosineLsh(vec=query_vec)
                elif index.similarity == "l2":
                    query = NearestNeighborsQuery.L2Lsh(vec=query_vec)
            elif index.model == "exact":
                if index.similarity == "cosine":
                    similarity = Similarity.Cosine
                elif index.similarity == "l2":
                    similarity = Similarity.L2
                query = NearestNeighborsQuery.Exact(
                    vec=query_vec, similarity=similarity
                )

            knn_neighbors = es.nearest_neighbors(
                index=index_name,
                query=query,
                id_field=dataset.id_field,
                k=k,
                fetch_source=fetch_source,
            )
            knn_result = []
            for result in knn_neighbors["hits"]["hits"]:
                knn_result.append(
                    (result["fields"][f"{dataset.id_field}"][0], result["_score"])
                )
            results[f"{index_name}"] = knn_result

        except NotFoundError:
            es.close()
            raise ValueError(
                f"Error: `{query_id}` did not match any value for the "
                f"keyword `{index.embedding_space.dataset.id_field}` at the index `{index.name}`"
            )
    es.close()

    return results, query_id


def compare_spaces(
    embedding_space_a,
    embedding_space_b,
    metric_a: str = "euclidean",
    metric_b: str = "euclidean",
    allow_precompute_knn: bool = False,
    histogram: bool = False,
):

    try:
        KNNBulkRelationship.get(
            embedding_space=EmbeddingSpace.get(name=embedding_space_a),
            metric=metric_a,
        )
    except KNNBulkRelationship.DoesNotExist:
        if allow_precompute_knn:
            KNNBulkOperations(embedding_space_name=embedding_space_a).index(
                metric=metric_a
            )
        else:
            raise OperationNotAllowedError(
                "Expensive operation not allowed. Cannot precompute KNN."
            )

    try:
        KNNBulkRelationship.get(
            embedding_space=EmbeddingSpace.get(name=embedding_space_b),
            metric=metric_b,
        )
    except KNNBulkRelationship.DoesNotExist:
        if allow_precompute_knn:
            KNNBulkOperations(embedding_space_name=embedding_space_b).index(
                metric=metric_b
            )
        else:
            raise OperationNotAllowedError(
                "Expensive operation not allowed. Cannot precompute KNN."
            )

    id_similarity_dict = KNNBulkOperations.space_similarity(
        embedding_space_name_a=embedding_space_a,
        metric_a=metric_a,
        embedding_space_name_b=embedding_space_b,
        metric_b=metric_b,
    )

    spaces_similarity = np.array(list(id_similarity_dict.values())).mean()

    fig, ax = (None, None)
    if histogram:
        similarity = np.array([i for i in id_similarity_dict.values()])

        density, bins = np.histogram(
            similarity, np.arange(0.0, 1.1, 0.1), normed=True, density=True
        )
        unity_density = density / density.sum()
        bins = [
            "<0.1",
            "<0.2",
            "<0.3",
            "<0.4",
            "<0.5",
            "<0.6",
            "<0.7",
            "<0.8",
            "<0.9",
            "<1.0",
        ]
        fig, ax = plt.subplots()

        ax.bar(bins[:], unity_density)
        fig.tight_layout()

    return spaces_similarity, id_similarity_dict, fig, ax
