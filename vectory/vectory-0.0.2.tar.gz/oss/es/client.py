"""Forked from
https://github.com/alexklibisz/elastiknn/tree/master/client-python/elastiknn"""

import multiprocessing
from typing import Dict, Iterable, List

from elasticsearch import Elasticsearch
from elasticsearch.helpers import parallel_bulk
from tqdm import tqdm

from .api import Mapping, NearestNeighborsQuery, Vec


class ElastiKNNClient:
    def __init__(self, es: Elasticsearch = None):
        """Wrapper on the official `elasticsearch.Elasticsearch` client for making
        Elastiknn requests.
        Parameters
        ----------
        es : `elasticsearch.Elasticsearch` client.
            This client is used internally to make all requests.
            Defaults to a client pointing at http://localhost:9200.
        """
        if es is None:
            self.es = Elasticsearch(["http://localhost:9200"], timeout=99)
        else:
            self.es = es

    def close(self):
        self.es.close()

    def delete_index(self, index_name):
        self.es.indices.delete(index=index_name, ignore=[404])

    def create_index(
        self,
        index_name: str,
        mapping: Mapping.Base,
        header_mapping: dict,
        number_of_shards: int = 1,
    ):
        """
        Update the mapping at the given index and field to store an Elastiknn vector.

        Parameters
        ----------
        index_name : string
            Name of the index to create for knn search
        mapping : instance of `Mapping.Base`
            Mapping object defining the vector's storage properties.
        header_mapping : dict
            Mapping that defines the metadata fields that will be stored in the index.
        number_of_shards : int
            Number of shards to use for the index. Elastiknn queries execute once per
            shard in parallel, you can generally speed up your queries by adding more
            shards to the index. Defaults to 1.

        Returns
        -------
        Dict
            Json response as a dict. Successful request returns
            `{"acknowledged": true}`.
        """
        index_settings = {"number_of_shards": number_of_shards, "elastiknn": True}
        index_mappings = {
            "properties": {
                "embedding": mapping.to_dict(),
                **header_mapping,
            }
        }

        return self.es.indices.create(
            index=index_name,
            settings=index_settings,
            mappings=index_mappings,
        )

    def index(
        self,
        index: str,
        vecs: Iterable[Vec.Base],
        metadata: List[dict],
        id_field: str,
        refresh: bool = False,
        num_threads: int = max(2, multiprocessing.cpu_count() - 2),
        chunk_size: int = 1000,
    ) -> int:
        """Index (i.e. store) the given vectors at the given index and field with the
        optional ids.

        Parameters
        ----------
        index : string
            Index where the vectors are stored.
        vecs : List of `Vec.Base`
            Vectors that should be indexed.
        metadata : List of Dicts
            Metadata associated with the given vectors. Should have same length as vecs.
        id_field:
            Field containing the document ID. Uses `store: true` setting as an
            optimization for faster id-only queries.
        refresh : bool
            Whether to refresh before returning. Set to true if you want to immediately
            run queries after indexing.
        num_threads : int
            Number of threads to use for indexing.
        chunk_size : int
            Number of vectors to index in a single bulk request.

        Returns
        -------
        Int
            Number of vectors successfully indexed.
        """

        def gen():
            for vec, vec_metadata in zip(vecs, metadata):
                yield {
                    "_op_type": "index",
                    "_index": index,
                    "_id": str(vec_metadata.get(id_field)),
                    "embedding": vec.to_dict(),
                    **vec_metadata,
                }

        succeses = 0
        for ok, _ in tqdm(
            parallel_bulk(
                client=self.es,
                actions=gen(),
                thread_count=num_threads,
                chunk_size=chunk_size,
            )
        ):
            succeses += ok

        if refresh:
            self.es.indices.refresh(index=index)

        return succeses

    def list_indices(self) -> List[str]:
        index_names = []
        for index_json in self.es.cat.indices(format="json"):
            index_names.append(index_json["index"])  # type: ignore
        return index_names

    def nearest_neighbors(
        self,
        index: str,
        query: NearestNeighborsQuery.Base,
        id_field: str,
        k: int = 10,
        fetch_source: bool = False,
    ) -> Dict:
        """Build and execute a nearest neighbors query against the given index.

        Parameters
        ----------
        index : string
            Index to run the search against.
        query : NearestNeighborsQuery.Base
            Query object defining the query properties.
        id_field:
            Field containing the document ID. Uses `store: true` setting as an
            optimization for faster id-only queries.
        k: int
            Number of hits to return.
        fetch_source : bool
            Whether to return the `_source` of the document. If you only need the ID,
            it's generally much faster to set this to False and instead of accessing
            the ID in hit['_id'], it will be in hit['fields'][id_field][0].

        Returns
        -------
        Dict
            Standard Elasticsearch search response parsed as a dict.
        """
        query_body = {"elastiknn_nearest_neighbors": query.to_dict()}
        if fetch_source:
            return self.es.search(index=index, query=query_body, size=k)
        else:
            return self.es.search(
                index=index,
                query=query_body,
                size=k,
                _source=fetch_source,
                docvalue_fields=[id_field],
                stored_fields="_none_",
                filter_path=[f"hits.hits.fields.{id_field}", "hits.hits._score"],
            )
