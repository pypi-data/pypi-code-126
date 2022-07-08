from typing import List, Tuple

import pynndescent
from peewee import chunked, IntegrityError

from oss.es.utils import load_embeddings_from_numpy, load_csv_with_headers
from oss.db.models import (
    KNNBulkStorage,
    EmbeddingSpace,
    KNNBulkRelationship,
)


database = EmbeddingSpace._meta.database

FIELD_NAMES = [
    "relationship",
    "npz_index",
    "k_1",
    "k_2",
    "k_3",
    "k_4",
    "k_5",
    "k_6",
    "k_7",
    "k_8",
    "k_9",
    "k_10",
]


class KNNBulkOperations:
    def __init__(self, embedding_space_name: str) -> None:
        self.embedding_space_name = embedding_space_name

        try:
            self.embedding_space = EmbeddingSpace.get(
                EmbeddingSpace.name == self.embedding_space_name
            )
        except EmbeddingSpace.DoesNotExist:
            raise Exception(
                f"EmbeddingSpace {self.embedding_space_name} does not exist."
            )

    def insert_datatuples_to_db(self, data_tuple: List[Tuple]) -> None:
        with database.atomic():
            for batch in chunked(data_tuple, 100):
                KNNBulkStorage.insert_many(batch, fields=FIELD_NAMES).execute()

    def index(self, metric: str) -> None:
        try:
            KNNBulkRelationship.create(
                embedding_space=self.embedding_space, metric=metric
            )
        except IntegrityError:
            raise Exception(
                f"KNN already calculated for embedding space "
                f"{self.embedding_space_name} with metric {metric}"
            ) from None

        knn_relationship = KNNBulkRelationship.get(
            embedding_space=self.embedding_space, metric=metric
        )

        embeddings = load_embeddings_from_numpy(self.embedding_space.npz_path)

        # Expensive operation
        index = pynndescent.NNDescent(embeddings, metric=metric, verbose=True)
        index.prepare()

        knn_indices, _ = index.query(embeddings, k=10)

        data_tuple = [
            (knn_relationship, i) + (data)
            for i, data in enumerate(list(map(tuple, knn_indices)))
        ]

        self.insert_datatuples_to_db(data_tuple)

    @staticmethod
    def jaccard_similarity(list1, list2):
        s1 = set(list1)
        s2 = set(list2)
        return float(len(s1.intersection(s2)) / len(s1.union(s2)))

    @staticmethod
    def get_knn(embeddings_space_name: str, metric: str):
        query = KNNBulkStorage.get_knn(
            embedding_space_name=embeddings_space_name, metric=metric
        )
        cursor = database.execute(query)

        return [knn for knn in cursor]

    @staticmethod
    def space_similarity(
        embedding_space_name_a: str,
        metric_a: str,
        embedding_space_name_b: str,
        metric_b: str,
    ):
        print(embedding_space_name_a, metric_a, embedding_space_name_b, metric_b)
        knn_a = KNNBulkOperations.get_knn(embedding_space_name_a, metric_a)
        knn_b = KNNBulkOperations.get_knn(embedding_space_name_b, metric_b)

        embedding_space_a = EmbeddingSpace.get(name=embedding_space_name_a)

        assert len(knn_a) == len(knn_b)
        rows, _, header = load_csv_with_headers(
            embedding_space_a.dataset.csv_path
        )
        id_field = embedding_space_a.dataset.id_field

        return dict(
            [
                (
                    rows[i][id_field],
                    KNNBulkOperations.jaccard_similarity(knn_a[i], knn_b[i]),
                )
                for i in range(len(knn_a))
            ]
        )
