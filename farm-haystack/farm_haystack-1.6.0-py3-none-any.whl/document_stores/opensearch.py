from typing import List, Optional, Union, Dict, Any

import logging
from copy import deepcopy

import numpy as np
from tqdm.auto import tqdm

try:
    from elasticsearch.helpers import bulk
    from elasticsearch.exceptions import RequestError
except (ImportError, ModuleNotFoundError) as ie:
    from haystack.utils.import_utils import _optional_component_not_installed

    _optional_component_not_installed(__name__, "elasticsearch", ie)


from haystack.schema import Document
from haystack.document_stores.base import get_batches_from_generator
from haystack.document_stores.filter_utils import LogicalFilterClause

from .elasticsearch import ElasticsearchDocumentStore


logger = logging.getLogger(__name__)


class OpenSearchDocumentStore(ElasticsearchDocumentStore):
    def __init__(
        self,
        scheme: str = "https",  # Mind this different default param
        username: str = "admin",  # Mind this different default param
        password: str = "admin",  # Mind this different default param
        host: Union[str, List[str]] = "localhost",
        port: Union[int, List[int]] = 9200,
        api_key_id: Optional[str] = None,
        api_key: Optional[str] = None,
        aws4auth=None,
        index: str = "document",
        label_index: str = "label",
        search_fields: Union[str, list] = "content",
        content_field: str = "content",
        name_field: str = "name",
        embedding_field: str = "embedding",
        embedding_dim: int = 768,
        custom_mapping: Optional[dict] = None,
        excluded_meta_data: Optional[list] = None,
        analyzer: str = "standard",
        ca_certs: Optional[str] = None,
        verify_certs: bool = False,  # Mind this different default param
        recreate_index: bool = False,
        create_index: bool = True,
        refresh_type: str = "wait_for",
        similarity: str = "dot_product",
        timeout: int = 30,
        return_embedding: bool = False,
        duplicate_documents: str = "overwrite",
        index_type: str = "flat",
        scroll: str = "1d",
        skip_missing_embeddings: bool = True,
        synonyms: Optional[List] = None,
        synonym_type: str = "synonym",
        use_system_proxy: bool = False,
    ):
        """
        Document Store using OpenSearch (https://opensearch.org/). It is compatible with the AWS Elasticsearch Service.

        In addition to native Elasticsearch query & filtering, it provides efficient vector similarity search using
        the KNN plugin that can scale to a large number of documents.

        :param host: url(s) of elasticsearch nodes
        :param port: port(s) of elasticsearch nodes
        :param username: username (standard authentication via http_auth)
        :param password: password (standard authentication via http_auth)
        :param api_key_id: ID of the API key (altenative authentication mode to the above http_auth)
        :param api_key: Secret value of the API key (altenative authentication mode to the above http_auth)
        :param aws4auth: Authentication for usage with aws elasticsearch (can be generated with the requests-aws4auth package)
        :param index: Name of index in elasticsearch to use for storing the documents that we want to search. If not existing yet, we will create one.
        :param label_index: Name of index in elasticsearch to use for storing labels. If not existing yet, we will create one.
        :param search_fields: Name of fields used by BM25Retriever to find matches in the docs to our incoming query (using elastic's multi_match query), e.g. ["title", "full_text"]
        :param content_field: Name of field that might contain the answer and will therefore be passed to the Reader Model (e.g. "full_text").
                           If no Reader is used (e.g. in FAQ-Style QA) the plain content of this field will just be returned.
        :param name_field: Name of field that contains the title of the the doc
        :param embedding_field: Name of field containing an embedding vector (Only needed when using a dense retriever (e.g. DensePassageRetriever, EmbeddingRetriever) on top)
                                Note, that in OpenSearch the similarity type for efficient approximate vector similarity calculations is tied to the embedding field's data type which cannot be changed after creation.
        :param embedding_dim: Dimensionality of embedding vector (Only needed when using a dense retriever (e.g. DensePassageRetriever, EmbeddingRetriever) on top)
        :param custom_mapping: If you want to use your own custom mapping for creating a new index in Elasticsearch, you can supply it here as a dictionary.
        :param analyzer: Specify the default analyzer from one of the built-ins when creating a new Elasticsearch Index.
                         Elasticsearch also has built-in analyzers for different languages (e.g. impacting tokenization). More info at:
                         https://www.elastic.co/guide/en/elasticsearch/reference/7.9/analysis-analyzers.html
        :param excluded_meta_data: Name of fields in Elasticsearch that should not be returned (e.g. [field_one, field_two]).
                                   Helpful if you have fields with long, irrelevant content that you don't want to display in results (e.g. embedding vectors).
        :param scheme: 'https' or 'http', protocol used to connect to your elasticsearch instance
        :param ca_certs: Root certificates for SSL: it is a path to certificate authority (CA) certs on disk. You can use certifi package with certifi.where() to find where the CA certs file is located in your machine.
        :param verify_certs: Whether to be strict about ca certificates
        :param create_index: Whether to try creating a new index (If the index of that name is already existing, we will just continue in any case
        :param refresh_type: Type of ES refresh used to control when changes made by a request (e.g. bulk) are made visible to search.
                             If set to 'wait_for', continue only after changes are visible (slow, but safe).
                             If set to 'false', continue directly (fast, but sometimes unintuitive behaviour when docs are not immediately available after ingestion).
                             More info at https://www.elastic.co/guide/en/elasticsearch/reference/6.8/docs-refresh.html
        :param similarity: The similarity function used to compare document vectors. 'dot_product' is the default since it is
                           more performant with DPR embeddings. 'cosine' is recommended if you are using a Sentence BERT model.
                           Note, that the use of efficient approximate vector calculations in OpenSearch is tied to embedding_field's data type which cannot be changed after creation.
                           You won't be able to use approximate vector calculations on an embedding_field which was created with a different similarity value.
                           In such cases a fallback to exact but slow vector calculations will happen and a warning will be displayed.
        :param timeout: Number of seconds after which an ElasticSearch request times out.
        :param return_embedding: To return document embedding
        :param duplicate_documents: Handle duplicates document based on parameter options.
                                    Parameter options : ( 'skip','overwrite','fail')
                                    skip: Ignore the duplicates documents
                                    overwrite: Update any existing documents with the same ID when adding documents.
                                    fail: an error is raised if the document ID of the document being added already
                                    exists.
        :param index_type: The type of index to be created. Choose from 'flat' and 'hnsw'.
                           As OpenSearch currently does not support all similarity functions (e.g. dot_product) in exact vector similarity calculations,
                           we don't make use of exact vector similarity when index_type='flat'. Instead we use the same approximate vector similarity calculations like in 'hnsw', but further optimized for accuracy.
                           Exact vector similarity is only used as fallback when there's a mismatch between certain requested and indexed similarity types.
                           In these cases however, a warning will be displayed. See similarity param for more information.
        :param scroll: Determines how long the current index is fixed, e.g. during updating all documents with embeddings.
                       Defaults to "1d" and should not be larger than this. Can also be in minutes "5m" or hours "15h"
                       For details, see https://www.elastic.co/guide/en/elasticsearch/reference/current/scroll-api.html
        :param skip_missing_embeddings: Parameter to control queries based on vector similarity when indexed documents miss embeddings.
                                        Parameter options: (True, False)
                                        False: Raises exception if one or more documents do not have embeddings at query time
                                        True: Query will ignore all documents without embeddings (recommended if you concurrently index and query)
        :param synonyms: List of synonyms can be passed while elasticsearch initialization.
                         For example: [ "foo, bar => baz",
                                        "foozball , foosball" ]
                         More info at https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-synonym-tokenfilter.html
        :param synonym_type: Synonym filter type can be passed.
                             Synonym or Synonym_graph to handle synonyms, including multi-word synonyms correctly during the analysis process.
                             More info at https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-synonym-graph-tokenfilter.html
        """
        self.embeddings_field_supports_similarity = False
        self.similarity_to_space_type = {"cosine": "cosinesimil", "dot_product": "innerproduct", "l2": "l2"}
        self.space_type_to_similarity = {v: k for k, v in self.similarity_to_space_type.items()}
        super().__init__(
            scheme=scheme,
            username=username,
            password=password,
            host=host,
            port=port,
            api_key_id=api_key_id,
            api_key=api_key,
            aws4auth=aws4auth,
            index=index,
            label_index=label_index,
            search_fields=search_fields,
            content_field=content_field,
            name_field=name_field,
            embedding_field=embedding_field,
            embedding_dim=embedding_dim,
            custom_mapping=custom_mapping,
            excluded_meta_data=excluded_meta_data,
            analyzer=analyzer,
            ca_certs=ca_certs,
            verify_certs=verify_certs,
            recreate_index=recreate_index,
            create_index=create_index,
            refresh_type=refresh_type,
            similarity=similarity,
            timeout=timeout,
            return_embedding=return_embedding,
            duplicate_documents=duplicate_documents,
            index_type=index_type,
            scroll=scroll,
            skip_missing_embeddings=skip_missing_embeddings,
            synonyms=synonyms,
            synonym_type=synonym_type,
            use_system_proxy=use_system_proxy,
        )

    def query_by_embedding(
        self,
        query_emb: np.ndarray,
        filters: Optional[Dict[str, Union[Dict, List, str, int, float, bool]]] = None,
        top_k: int = 10,
        index: Optional[str] = None,
        return_embedding: Optional[bool] = None,
        headers: Optional[Dict[str, str]] = None,
        scale_score: bool = True,
    ) -> List[Document]:
        """
        Find the document that is most similar to the provided `query_emb` by using a vector similarity metric.

        :param query_emb: Embedding of the query (e.g. gathered from DPR)
        :param filters: Optional filters to narrow down the search space to documents whose metadata fulfill certain
                        conditions.
                        Filters are defined as nested dictionaries. The keys of the dictionaries can be a logical
                        operator (`"$and"`, `"$or"`, `"$not"`), a comparison operator (`"$eq"`, `"$in"`, `"$gt"`,
                        `"$gte"`, `"$lt"`, `"$lte"`) or a metadata field name.
                        Logical operator keys take a dictionary of metadata field names and/or logical operators as
                        value. Metadata field names take a dictionary of comparison operators as value. Comparison
                        operator keys take a single value or (in case of `"$in"`) a list of values as value.
                        If no logical operator is provided, `"$and"` is used as default operation. If no comparison
                        operator is provided, `"$eq"` (or `"$in"` if the comparison value is a list) is used as default
                        operation.

                            __Example__:
                            ```python
                            filters = {
                                "$and": {
                                    "type": {"$eq": "article"},
                                    "date": {"$gte": "2015-01-01", "$lt": "2021-01-01"},
                                    "rating": {"$gte": 3},
                                    "$or": {
                                        "genre": {"$in": ["economy", "politics"]},
                                        "publisher": {"$eq": "nytimes"}
                                    }
                                }
                            }
                            # or simpler using default operators
                            filters = {
                                "type": "article",
                                "date": {"$gte": "2015-01-01", "$lt": "2021-01-01"},
                                "rating": {"$gte": 3},
                                "$or": {
                                    "genre": ["economy", "politics"],
                                    "publisher": "nytimes"
                                }
                            }
                            ```

                            To use the same logical operator multiple times on the same level, logical operators take
                            optionally a list of dictionaries as value.

                            __Example__:
                            ```python
                            filters = {
                                "$or": [
                                    {
                                        "$and": {
                                            "Type": "News Paper",
                                            "Date": {
                                                "$lt": "2019-01-01"
                                            }
                                        }
                                    },
                                    {
                                        "$and": {
                                            "Type": "Blog Post",
                                            "Date": {
                                                "$gte": "2019-01-01"
                                            }
                                        }
                                    }
                                ]
                            }
                            ```
        :param top_k: How many documents to return
        :param index: Index name for storing the docs and metadata
        :param return_embedding: To return document embedding
        :param headers: Custom HTTP headers to pass to elasticsearch client (e.g. {'Authorization': 'Basic YWRtaW46cm9vdA=='})
                Check out https://www.elastic.co/guide/en/elasticsearch/reference/current/http-clients.html for more information.
        :param scale_score: Whether to scale the similarity score to the unit interval (range of [0,1]).
                            If true (default) similarity scores (e.g. cosine or dot_product) which naturally have a different value range will be scaled to a range of [0,1], where 1 means extremely relevant.
                            Otherwise raw similarity scores (e.g. cosine or dot_product) will be used.
        :return:
        """
        if index is None:
            index = self.index

        if return_embedding is None:
            return_embedding = self.return_embedding

        if not self.embedding_field:
            raise RuntimeError("Please specify arg `embedding_field` in ElasticsearchDocumentStore()")
        # +1 in similarity to avoid negative numbers (for cosine sim)
        body: Dict[str, Any] = {"size": top_k, "query": self._get_vector_similarity_query(query_emb, top_k)}
        if filters:
            body["query"]["bool"]["filter"] = LogicalFilterClause.parse(filters).convert_to_elasticsearch()

        excluded_meta_data: Optional[list] = None

        if self.excluded_meta_data:
            excluded_meta_data = deepcopy(self.excluded_meta_data)

            if return_embedding is True and self.embedding_field in excluded_meta_data:
                excluded_meta_data.remove(self.embedding_field)
            elif return_embedding is False and self.embedding_field not in excluded_meta_data:
                excluded_meta_data.append(self.embedding_field)
        elif return_embedding is False:
            excluded_meta_data = [self.embedding_field]

        if excluded_meta_data:
            body["_source"] = {"excludes": excluded_meta_data}

        logger.debug(f"Retriever query: {body}")
        result = self.client.search(index=index, body=body, request_timeout=300, headers=headers)["hits"]["hits"]

        documents = [
            self._convert_es_hit_to_document(
                hit, adapt_score_for_embedding=True, return_embedding=return_embedding, scale_score=scale_score
            )
            for hit in result
        ]
        return documents

    def _create_document_index(self, index_name: str, headers: Optional[Dict[str, str]] = None):
        """
        Create a new index for storing documents.
        """
        # Check if index_name refers to an alias
        if self.client.indices.exists_alias(name=index_name):
            logger.debug(f"Index name {index_name} is an alias.")

        # check if the existing index has the embedding field; if not create it
        if self.client.indices.exists(index=index_name, headers=headers):
            indices = self.client.indices.get(index_name, headers=headers)
            # If the index name is an alias that groups multiple existing indices, each of them must have an embedding_field.
            for index_id, index_info in indices.items():
                mappings = index_info["mappings"]
                index_settings = index_info["settings"]["index"]
                if self.search_fields:
                    for search_field in self.search_fields:
                        if (
                            search_field in mappings["properties"]
                            and mappings["properties"][search_field]["type"] != "text"
                        ):
                            raise Exception(
                                f"The search_field '{search_field}' of index '{index_id}' with type '{mappings['properties'][search_field]['type']}' "
                                f"does not have the right type 'text' to be queried in fulltext search. Please use only 'text' type properties as search_fields or use another index. "
                                f"This error might occur if you are trying to use haystack 1.0 and above with an existing elasticsearch index created with a previous version of haystack. "
                                f'In this case deleting the index with `delete_index(index="{index_id}")` will fix your environment. '
                                f"Note, that all data stored in the index will be lost!"
                            )

                # embedding field will be created
                if self.embedding_field not in mappings["properties"]:
                    mappings["properties"][self.embedding_field] = self._get_embedding_field_mapping(
                        similarity=self.similarity
                    )
                    self.client.indices.put_mapping(index=index_id, body=mappings, headers=headers)
                    self.embeddings_field_supports_similarity = True
                else:
                    # bad embedding field
                    if mappings["properties"][self.embedding_field]["type"] != "knn_vector":
                        raise Exception(
                            f"The '{index_id}' index in OpenSearch already has a field called '{self.embedding_field}'"
                            f" with the type '{mappings['properties'][self.embedding_field]['type']}'. Please update the "
                            f"document_store to use a different name for the embedding_field parameter."
                        )
                    # embedding field with global space_type setting
                    if "method" not in mappings["properties"][self.embedding_field]:
                        embedding_field_space_type = index_settings["knn.space_type"]
                    # embedding field with local space_type setting
                    else:
                        # embedding field with global space_type setting
                        if "method" not in mappings["properties"][self.embedding_field]:
                            embedding_field_space_type = index_settings["knn.space_type"]
                        # embedding field with local space_type setting
                        else:
                            embedding_field_space_type = mappings["properties"][self.embedding_field]["method"][
                                "space_type"
                            ]

                        embedding_field_similarity = self.space_type_to_similarity[embedding_field_space_type]
                        if embedding_field_similarity == self.similarity:
                            self.embeddings_field_supports_similarity = True
                        else:
                            logger.warning(
                                f"Embedding field '{self.embedding_field}' is optimized for similarity '{embedding_field_similarity}'. "
                                f"Falling back to slow exact vector calculation. "
                                f"Consider cloning the embedding field optimized for '{embedding_field_similarity}' by calling clone_embedding_field(similarity='{embedding_field_similarity}', ...) "
                                f"or creating a new index optimized for '{self.similarity}' by setting `similarity='{self.similarity}'` the first time you instantiate OpenSearchDocumentStore for the new index, "
                                f"e.g. `OpenSearchDocumentStore(index='my_new_{self.similarity}_index', similarity='{self.similarity}')`."
                            )

                # Adjust global ef_search setting. If not set, default is 512.
                ef_search = index_settings.get("knn.algo_param", {"ef_search": 512}).get("ef_search", 512)
                if self.index_type == "hnsw" and ef_search != 20:
                    body = {"knn.algo_param.ef_search": 20}
                    self.client.indices.put_settings(index=index_id, body=body, headers=headers)
                elif self.index_type == "flat" and ef_search != 512:
                    body = {"knn.algo_param.ef_search": 512}
                    self.client.indices.put_settings(index=index_id, body=body, headers=headers)

            return

        if self.custom_mapping:
            index_definition = self.custom_mapping
        else:
            index_definition = {
                "mappings": {
                    "properties": {self.name_field: {"type": "keyword"}, self.content_field: {"type": "text"}},
                    "dynamic_templates": [
                        {"strings": {"path_match": "*", "match_mapping_type": "string", "mapping": {"type": "keyword"}}}
                    ],
                },
                "settings": {"analysis": {"analyzer": {"default": {"type": self.analyzer}}}},
            }

            if self.synonyms:
                for field in self.search_fields:
                    index_definition["mappings"]["properties"].update({field: {"type": "text", "analyzer": "synonym"}})
                index_definition["mappings"]["properties"][self.content_field] = {"type": "text", "analyzer": "synonym"}

                index_definition["settings"]["analysis"]["analyzer"]["synonym"] = {
                    "tokenizer": "whitespace",
                    "filter": ["lowercase", "synonym"],
                }
                index_definition["settings"]["analysis"]["filter"] = {
                    "synonym": {"type": self.synonym_type, "synonyms": self.synonyms}
                }

            else:
                for field in self.search_fields:
                    index_definition["mappings"]["properties"].update({field: {"type": "text"}})

            if self.embedding_field:
                index_definition["settings"]["index"] = {"knn": True}
                if self.index_type == "hnsw":
                    index_definition["settings"]["index"]["knn.algo_param.ef_search"] = 20
                index_definition["mappings"]["properties"][self.embedding_field] = self._get_embedding_field_mapping(
                    similarity=self.similarity
                )

        try:
            self.client.indices.create(index=index_name, body=index_definition, headers=headers)
        except RequestError as e:
            # With multiple workers we need to avoid race conditions, where:
            # - there's no index in the beginning
            # - both want to create one
            # - one fails as the other one already created it
            if not self.client.indices.exists(index=index_name, headers=headers):
                raise e

    def _get_embedding_field_mapping(self, similarity: str):
        space_type = self.similarity_to_space_type[similarity]
        method: dict = {"space_type": space_type, "name": "hnsw", "engine": "nmslib"}

        if self.index_type == "flat":
            # use default parameters from https://opensearch.org/docs/1.2/search-plugins/knn/knn-index/
            # we need to set them explicitly as aws managed instances starting from version 1.2 do not support empty parameters
            method["parameters"] = {"ef_construction": 512, "m": 16}
        elif self.index_type == "hnsw":
            method["parameters"] = {"ef_construction": 80, "m": 64}
        else:
            logger.error("Please set index_type to either 'flat' or 'hnsw'")

        embeddings_field_mapping = {"type": "knn_vector", "dimension": self.embedding_dim, "method": method}
        return embeddings_field_mapping

    def _create_label_index(self, index_name: str, headers: Optional[Dict[str, str]] = None):
        if self.client.indices.exists(index=index_name, headers=headers):
            return
        mapping = {
            "mappings": {
                "properties": {
                    "query": {"type": "text"},
                    "answer": {
                        "type": "nested"
                    },  # In elasticsearch we use type:flattened, but this is not supported in opensearch
                    "document": {"type": "nested"},
                    "is_correct_answer": {"type": "boolean"},
                    "is_correct_document": {"type": "boolean"},
                    "origin": {"type": "keyword"},  # e.g. user-feedback or gold-label
                    "document_id": {"type": "keyword"},
                    "no_answer": {"type": "boolean"},
                    "pipeline_id": {"type": "keyword"},
                    "created_at": {"type": "date", "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"},
                    "updated_at": {"type": "date", "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"}
                    # TODO add pipeline_hash and pipeline_name once we migrated the REST API to pipelines
                }
            }
        }
        try:
            self.client.indices.create(index=index_name, body=mapping, headers=headers)
        except RequestError as e:
            # With multiple workers we need to avoid race conditions, where:
            # - there's no index in the beginning
            # - both want to create one
            # - one fails as the other one already created it
            if not self.client.indices.exists(index=index_name, headers=headers):
                raise e

    def _get_vector_similarity_query(self, query_emb: np.ndarray, top_k: int):
        """
        Generate Elasticsearch query for vector similarity.
        """
        if self.embeddings_field_supports_similarity:
            query: dict = {
                "bool": {"must": [{"knn": {self.embedding_field: {"vector": query_emb.tolist(), "k": top_k}}}]}
            }
        else:
            # if we do not have a proper similarity field we have to fall back to exact but slow vector similarity calculation
            query = {
                "script_score": {
                    "query": {"match_all": {}},
                    "script": {
                        "source": "knn_score",
                        "lang": "knn",
                        "params": {
                            "field": self.embedding_field,
                            "query_value": query_emb.tolist(),
                            "space_type": self.similarity_to_space_type[self.similarity],
                        },
                    },
                }
            }
        return query

    def _get_raw_similarity_score(self, score):
        # adjust scores according to https://opensearch.org/docs/latest/search-plugins/knn/approximate-knn
        # and https://opensearch.org/docs/latest/search-plugins/knn/knn-score-script/
        if self.similarity == "dot_product":
            if score > 1:
                score = score - 1
            else:
                score = -(1 / score - 1)
        elif self.similarity == "l2":
            score = 1 / score - 1
        elif self.similarity == "cosine":
            if self.embeddings_field_supports_similarity:
                score = -(1 / score - 2)
            else:
                score = score - 1

        return score

    def clone_embedding_field(
        self,
        new_embedding_field: str,
        similarity: str,
        batch_size: int = 10_000,
        headers: Optional[Dict[str, str]] = None,
    ):
        mapping = self.client.indices.get(self.index, headers=headers)[self.index]["mappings"]
        if new_embedding_field in mapping["properties"]:
            raise Exception(
                f"{new_embedding_field} already exists with mapping {mapping['properties'][new_embedding_field]}"
            )
        mapping["properties"][new_embedding_field] = self._get_embedding_field_mapping(similarity=similarity)
        self.client.indices.put_mapping(index=self.index, body=mapping, headers=headers)

        document_count = self.get_document_count(headers=headers)
        result = self._get_all_documents_in_index(index=self.index, batch_size=batch_size, headers=headers)

        logging.getLogger("elasticsearch").setLevel(logging.CRITICAL)

        with tqdm(total=document_count, position=0, unit=" Docs", desc="Cloning embeddings") as progress_bar:
            for result_batch in get_batches_from_generator(result, batch_size):
                document_batch = [self._convert_es_hit_to_document(hit, return_embedding=True) for hit in result_batch]
                doc_updates = []
                for doc in document_batch:
                    if doc.embedding is not None:
                        update = {
                            "_op_type": "update",
                            "_index": self.index,
                            "_id": doc.id,
                            "doc": {new_embedding_field: doc.embedding.tolist()},
                        }
                        doc_updates.append(update)

                bulk(self.client, doc_updates, request_timeout=300, refresh=self.refresh_type, headers=headers)
                progress_bar.update(batch_size)


class OpenDistroElasticsearchDocumentStore(OpenSearchDocumentStore):
    """
    A DocumentStore which has an Open Distro for Elasticsearch service behind it.
    """

    def __init__(
        self,
        scheme: str = "https",
        username: str = "admin",
        password: str = "admin",
        host: Union[str, List[str]] = "localhost",
        port: Union[int, List[int]] = 9200,
        api_key_id: Optional[str] = None,
        api_key: Optional[str] = None,
        aws4auth=None,
        index: str = "document",
        label_index: str = "label",
        search_fields: Union[str, list] = "content",
        content_field: str = "content",
        name_field: str = "name",
        embedding_field: str = "embedding",
        embedding_dim: int = 768,
        custom_mapping: Optional[dict] = None,
        excluded_meta_data: Optional[list] = None,
        analyzer: str = "standard",
        ca_certs: Optional[str] = None,
        verify_certs: bool = False,
        recreate_index: bool = False,
        create_index: bool = True,
        refresh_type: str = "wait_for",
        similarity: str = "cosine",  # Mind this different default param
        timeout: int = 30,
        return_embedding: bool = False,
        duplicate_documents: str = "overwrite",
        index_type: str = "flat",
        scroll: str = "1d",
        skip_missing_embeddings: bool = True,
        synonyms: Optional[List] = None,
        synonym_type: str = "synonym",
        use_system_proxy: bool = False,
    ):
        logger.warning(
            "Open Distro for Elasticsearch has been replaced by OpenSearch! "
            "See https://opensearch.org/faq/ for details. "
            "We recommend using the OpenSearchDocumentStore instead."
        )
        super().__init__(
            scheme=scheme,
            username=username,
            password=password,
            host=host,
            port=port,
            api_key_id=api_key_id,
            api_key=api_key,
            aws4auth=aws4auth,
            index=index,
            label_index=label_index,
            search_fields=search_fields,
            content_field=content_field,
            name_field=name_field,
            embedding_field=embedding_field,
            embedding_dim=embedding_dim,
            custom_mapping=custom_mapping,
            excluded_meta_data=excluded_meta_data,
            analyzer=analyzer,
            ca_certs=ca_certs,
            verify_certs=verify_certs,
            recreate_index=recreate_index,
            create_index=create_index,
            refresh_type=refresh_type,
            similarity=similarity,
            timeout=timeout,
            return_embedding=return_embedding,
            duplicate_documents=duplicate_documents,
            index_type=index_type,
            scroll=scroll,
            skip_missing_embeddings=skip_missing_embeddings,
            synonyms=synonyms,
            synonym_type=synonym_type,
            use_system_proxy=use_system_proxy,
        )
