import multiprocessing
import sys
from typing import List, Union

import numpy as np
from elasticsearch import Elasticsearch, RequestError, NotFoundError
from elasticsearch_dsl import Search
from elasticsearch.helpers import parallel_bulk
from tqdm import tqdm


class ElasticClient:
    def __init__(
        self,
        host: str = "localhost",
        port: str = "9200",
    ):
        self.host = host
        self.port = port
        self.connect()

    def connect(self):
        self.client: Elasticsearch = Elasticsearch(
            f"http://{self.host}:{self.port}",
            timeout=99,
        )

    def close(self):
        self.client.close()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def create_index(
        self,
        index_name: str,
        header_mapping: dict,
        dims: int,
        model: str = "lsh",
        similarity: str = "cosine",
        L: int = 99,
        k: int = 1,
        w: int = 3,
    ) -> None:

        extra_params = (
            {"L": L, "k": k, "w": w} if similarity == "l2" else {"L": L, "k": k}
        )

        if model == "exact":
            model_params = {"dims": dims}
        else:
            model_params = {
                "dims": dims,
                "model": model,  # type: ignore
                "similarity": similarity,  # type: ignore
                **extra_params,
            }

        index_settings = {
            "settings": {"number_of_shards": 1, "elastiknn": True},
            "mappings": {
                "properties": {
                    "embedding": {
                        "type": "elastiknn_dense_float_vector",
                        "elastiknn": {**model_params},
                    },
                    **header_mapping,
                }
            },
        }

        try:
            self.client.indices.create(
                index=index_name,
                settings=index_settings["settings"],  # type: ignore
                mappings=index_settings["mappings"],  # type: ignore
            )

            print(f"Index {index_name} created!")

        except RequestError as e:
            if e.status_code == 400:
                sys.exit(f"Index {index_name} already exists!")
            else:
                raise e

    def generate_actions(self, rows: List[dict], embeddings: np.ndarray):
        for idx, row in enumerate(rows):
            yield {"embedding": embeddings[idx].tolist(), **row}

    def load_embeddings(
        self,
        index_name: str,
        rows: List[dict],
        embeddings: np.ndarray,
        num_threads: int = multiprocessing.cpu_count(),
        chunk_size: int = 1000,
    ) -> int:

        succeses = 0
        for ok, _ in tqdm(
            parallel_bulk(
                client=self.client,
                index=index_name,
                actions=self.generate_actions(rows, embeddings),
                thread_count=num_threads,
                chunk_size=chunk_size,
            )
        ):
            succeses += ok

        return succeses

    def delete_index(self, index_name: str) -> None:
        self.client.indices.delete(index=index_name, ignore=[404])

    def list_indices(self) -> List[str]:
        index_names = []
        for index_json in self.client.cat.indices(format="json"):
            index_names.append(index_json["index"])  # type: ignore
        return index_names

    def match_query(
        self,
        index_name: str,
        keyword: str,
        value: Union[str, int, float],
        k: int = 10,
        similarity: str = "cosine",
    ) -> List:
        s = Search(using=self.client, index=index_name).query(
            "match", **{keyword: value}
        )
        response = s.execute()
        if len(response) == 0:
            raise NotFoundError
        embedding_es_id = response["hits"]["hits"][0]["_id"]

        properties = self.client.indices.get_mapping(index=index_name)[index_name][
            "mappings"
        ]["properties"]["embedding"]["elastiknn"]

        if properties["model"] == "exact":
            query_options = {"model": "exact", "similarity": similarity}
        else:
            query_options = {
                "model": properties["model"],
                "similarity": properties.get("similarity", "cosine"),
                "candidates": k * 100,  # type: ignore
                "probes": 2,  # type: ignore
            }

        query_body = {
            "elastiknn_nearest_neighbors": {
                "field": "embedding",
                "vec": {
                    "index": index_name,
                    "field": "embedding",
                    "id": embedding_es_id,
                },
                **query_options,
            }
        }
        response = self.client.search(index=index_name, query=query_body, size=k)

        k_nearest = []
        for res in response["hits"]["hits"]:
            score = res["_score"]
            id = res["_id"]
            res = res["_source"]
            res.pop("embedding")
            res["score"] = score
            res["_id"] = id
            k_nearest.append(res)

        return k_nearest
