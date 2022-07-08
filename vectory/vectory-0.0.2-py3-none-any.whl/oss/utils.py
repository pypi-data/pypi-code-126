from dataclasses import dataclass
from unicodedata import name
from oss.db.models import EmbeddingSpace, ElasticSearchIndex
from oss.es.client import ElastiKNNClient
from typing import Union
import typer
from oss.es.api import Mapping
import oss.oss.main


# @dataclass
# class dataset:
#     name: str
#     csv_path: str
#     id_field: str


# @dataclass
# class experiment:
#     name: str
#     train_dataset: dataset
#     model: str
#     params: Union[dict, str]


# @dataclass
# class embedding_space:
#     name: str
#     npz_path: str
#     dims: int
#     experiment: experiment
#     dataset: dataset


def edit_es_indices(indices, obj, column, new_value, table):
    if (len(indices) != 0) and column in [
        "id_field",
        "csv_path",
        "dims",
        "npz_path",
    ]:
        typer.echo(
            f"WARNING: Changing the csv_path of the dataset {obj.name} will cause the"
            + "next indices to be loaded again.\n"
        )
        for index in indices:
            typer.echo(f"- {index.name}")
        confirmation = typer.confirm("Are you sure you want to continue?")
        if not confirmation:
            typer.echo("Edition aborted!")
            raise typer.Abort()
        for index in indices:

            name = index.name
            embedding_space = index.embedding_space
            model = index.model
            similarity = index.similarity
            num_threads = index.num_threads
            chunk_size = index.chunk_size
            k = index.k
            L = index.L
            w = index.w
            number_of_shards = index.number_of_shards
            if model == "lsh":
                if similarity == "cosine":
                    mapping = Mapping.CosineLsh(dims=embedding_space.dims, L=L, k=k)
                elif similarity == "l2":
                    mapping = Mapping.L2Lsh(dims=embedding_space.dims, L=L, k=k, w=w)
            elif model == "exact":
                mapping = Mapping.DenseFloat(dims=embedding_space.dims)

            # index_data = list(
            # ElasticSearchIndex.select().where(ElasticSearchIndex.name == "v1").dicts()
            # )[0]
            es = ElastiKNNClient()
            es.delete_index(index_name=index.name)
            index.delete_instance()
            setattr(obj, column, new_value)
            updated_rows = table.bulk_update([obj], fields=[getattr(table, column)])
            oss.oss.main.load_index(
                index_name=str(name),
                embedding_space_name=str(embedding_space.name),
                mapping=mapping,
                num_threads=num_threads,
                chunk_size=chunk_size,
                number_of_shards=number_of_shards,
            )
    else:
        setattr(obj, column, new_value)
        updated_rows = table.bulk_update([obj], fields=[getattr(table, column)])
    return updated_rows
