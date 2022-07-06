import dataclasses
import datetime
import hashlib
import json
import os
import random
import string
import tempfile
from dataclasses import dataclass
from typing import Any
from typing import Dict
from typing import Iterator
from typing import Union
from urllib.parse import urlparse

import boto3
import pandas

from tecton_athena.templates_utils import load_template
from tecton_core import conf
from tecton_core import logger as logger_lib
from tecton_core.errors import TectonAthenaValidationError
from tecton_spark import offline_store

logger = logger_lib.get_logger("AthenaSession")

# In some cases, strings in Pandas DF are actually represented as "object" types.
# Hence the sketchy 'object' -> 'string' map
PANDAS_TO_HIVE_TYPES = {"string": "string", "object": "string", "int64": "bigint", "float64": "double"}

S3_ATHENA_PANDAS_UPLOADS = "athena/pandas_uploads"

CREATE_TABLE_TEMPLATE = load_template("create_table.sql")


def _get_athena_database():
    return conf.get_or_none("ATHENA_DATABASE") or "tecton_temp_tables"


def _random_name():
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(10))


PARTITION_TYPE_DATESTR = "PARTITION_TYPE_DATESTR"
PARTITION_TYPE_UNIX_EPOCH_NS = "PARTITION_TYPE_UNIX_EPOCH_NS"
GLUE_CATALOG_TABLE_PROPERTY_HASH = "tecton_table_metadata_hash"
GLUE_CATALOG_TABLE_PROPERTY_SPEC_VERSION = "tecton_table_spec_version"


@dataclass
class AthenaTableCreationSpec:
    """Athena Table representation (registered in Glue)"""

    # SPEC_VERSION Explanation:
    # - The SDK will never overwrite a table registration that happened with a newer version
    # - Increment if you fundamentally change the way Athena tables, for an identical FeatureView, are registered
    #   For example, if you move away from partition projection
    # - The SPEC_VERSION must not be part of the stable_hash calculation - otherwise the SDK believes it needs to overwrite
    #   a table's registration, even if the metadata for that table is unchanged, just because the version is incremented
    # - A separate SPEC_VERSION is used here rather than relying on the SDK's version because most SDK versions will increment
    #   without ever incrementing the SPEC_VERSION here
    SPEC_VERSION = 1

    database: str
    table: str
    s3_location: str
    columns: Dict[str, str]
    partition_by: Union[offline_store.TIME_PARTITION, offline_store.ANCHOR_TIME]
    partition_by_type: str
    partition_by_format: str
    partition_by_range_from: str
    partition_by_range_to: str
    partition_by_interval: int
    partition_by_interval_timedelta: datetime.timedelta
    partition_type: Union[PARTITION_TYPE_DATESTR, PARTITION_TYPE_UNIX_EPOCH_NS]

    @property
    def _json_str(self):
        return json.dumps(
            dataclasses.asdict(self),
            default=str,
            sort_keys=True,
            indent=None,
            ensure_ascii=False,
            separators=(",", ":"),
        ).encode("utf-8")

    @property
    def stable_hash(self):
        str_representation = self._json_str
        return hashlib.md5(str_representation).hexdigest()


class AthenaSession:
    def __init__(self):
        self._athena_s3_bucket = None

    @property
    def _wr(self):
        try:
            import awswrangler

            return awswrangler
        except ModuleNotFoundError:
            raise Exception(
                "Athena Session cannot be initialized. Python module awswrangler not found. Did you forget to pip install tecton[athena]?"
            )

    def _get_athena_s3_bucket(self):
        s3_bucket = conf.get_or_none("ATHENA_S3_BUCKET")
        if s3_bucket is not None:
            # Configuration always takes precedent and can be set at any time
            self._athena_s3_bucket = s3_bucket
        elif self._athena_s3_bucket is None:
            # If the bucket hasn't been initialized yet, let's create a new bucket
            # Let's cache the result to ensure we don't do it unnecessarily over and over again
            self._athena_s3_bucket = self._wr.athena.create_athena_bucket()

        if self._athena_s3_bucket.endswith("/"):
            # Drop "/" - calling function expects a path without trailing "/"
            self._athena_s3_bucket = self._athena_s3_bucket[0:-1]

        return self._athena_s3_bucket

    def _delete_table_if_exists(self, database: str, table: str):
        return self._wr.catalog.delete_table_if_exists(database=database, table=table)

    def _get_table_parameters(self, database: str, table: str) -> Dict:
        return self._wr.catalog.get_table_parameters(database=database, table=table)

    def _does_table_exist(self, database: str, table: str) -> bool:
        return self._wr.catalog.does_table_exist(database=database, table=table)

    def _upload_pandas_to_s3(self, pandas_df: pandas.DataFrame):
        with tempfile.NamedTemporaryFile(suffix=".parquet.snappy") as f:
            s3_client = boto3.client("s3")
            pandas_df.to_parquet(f.name, compression="snappy")

            local_file_name = os.path.basename(f.name)
            s3_random_dir_name = _random_name()

            s3_object_directory = "/".join([S3_ATHENA_PANDAS_UPLOADS, s3_random_dir_name])
            s3_object_name = "/".join([s3_object_directory, local_file_name])

            s3_athena_bucket = self._get_athena_s3_bucket()
            s3_path_without_file = "/".join([s3_athena_bucket, s3_object_directory, ""])
            s3_full_path = "/".join([s3_athena_bucket, s3_object_name])
            logger.info(f"Writing pandas df to S3 at {s3_full_path}...")

            s3_bucket_without_prefix = urlparse(s3_athena_bucket).netloc

            # Consider switching to multipart upload
            # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3.html#multipart-transfers
            s3_client.upload_file(f.name, s3_bucket_without_prefix, s3_object_name)
            return s3_path_without_file

    def _create_athena_table_from_s3_path(self, s3_path: str, table_name: str, hive_columns: dict):
        athena_database = _get_athena_database()
        query = CREATE_TABLE_TEMPLATE.render(
            database=athena_database, table=table_name, s3_location=s3_path, columns=hive_columns
        )
        logger.info(f"Creating Athena table {athena_database}.{table_name}...")

        self.sql(query)

        logger.info(f"Table {athena_database}.{table_name} was successfully created")

        return f"{athena_database}.{table_name}"

    def _pandas_columns_to_hive_columns(self, pandas_df: pandas.DataFrame):
        column_types = {}
        for k, v in pandas_df.dtypes.to_dict().items():
            if "datetime64" in v.name:
                column_types[k] = "timestamp"
                continue
            type_name = v.name.lower()
            if type_name not in PANDAS_TO_HIVE_TYPES:
                raise Exception(f"Pandas Type {type_name} not supported. Mapping to Hive Type not found.")
            column_types[k] = PANDAS_TO_HIVE_TYPES[type_name]
        return column_types

    def write_pandas(self, df: pandas.DataFrame, table_name: str):
        s3_full_path = self._upload_pandas_to_s3(df)
        hive_columns = self._pandas_columns_to_hive_columns(df)

        return self._create_athena_table_from_s3_path(s3_full_path, table_name, hive_columns)

    def sql(self, sql_query: str) -> Union[str, Dict[str, Any]]:
        return self._wr.athena.start_query_execution(sql_query, database=_get_athena_database(), wait=True)

    def read_sql(self, sql_query: str) -> Union[pandas.DataFrame, Iterator[pandas.DataFrame]]:
        return self._wr.athena.read_sql_query(sql_query, database=_get_athena_database())

    def get_database(self) -> str:
        return _get_athena_database()

    def create_table(self, table_spec: AthenaTableCreationSpec):
        logger.info(f"Registering Glue table {table_spec.database}.{table_spec.table}...")
        sql = CREATE_TABLE_TEMPLATE.render(
            database=table_spec.database,
            table=table_spec.table,
            s3_location=table_spec.s3_location,
            columns=table_spec.columns,
            partition_by=table_spec.partition_by,
            partition_by_type=table_spec.partition_by_type,
            partition_by_format=table_spec.partition_by_format,
            partition_by_range_from=table_spec.partition_by_range_from,
            partition_by_range_to=table_spec.partition_by_range_to,
            partition_by_interval=table_spec.partition_by_interval,
            tecton_table_metadata_hash=table_spec.stable_hash,
            tecton_table_spec_version=AthenaTableCreationSpec.SPEC_VERSION,
        )
        self.sql(sql)

    def _is_existing_table_equivalent_to_spec(self, table_spec: AthenaTableCreationSpec):
        parameters = self._get_table_parameters(table_spec.database, table_spec.table)

        return parameters.get(GLUE_CATALOG_TABLE_PROPERTY_HASH) == table_spec.stable_hash

    def _get_existing_table_spec_version(self, table_spec: AthenaTableCreationSpec):
        parameters = self._get_table_parameters(table_spec.database, table_spec.table)
        if GLUE_CATALOG_TABLE_PROPERTY_SPEC_VERSION not in parameters:
            return None

        return int(parameters[GLUE_CATALOG_TABLE_PROPERTY_SPEC_VERSION])

    def create_table_if_necessary(self, table_spec: AthenaTableCreationSpec):
        if not self._does_table_exist(table_spec.database, table_spec.table):
            return self.create_table(table_spec)

        existing_table_spec_version = self._get_existing_table_spec_version(table_spec)

        if self._is_existing_table_equivalent_to_spec(table_spec):
            logger.debug(
                f"Glue table {table_spec.database}.{table_spec.table} hash matches expectation ({table_spec.stable_hash}). No update needed."
            )
        elif existing_table_spec_version is None:
            raise TectonAthenaValidationError(
                f"Glue table {table_spec.database}.{table_spec.table} registration doesn't meet expectations but cannot be updated because it doesn't seem to have been registered by Tecton. Please drop the table to have Tecton manage its registration."
            )
        elif existing_table_spec_version > AthenaTableCreationSpec.SPEC_VERSION:
            raise TectonAthenaValidationError(
                f"Glue table {table_spec.database}.{table_spec.table} registration doesn't meet expectations but cannot be updated because it was registered with a newer version of Tecton. Please upgrade the SDK. Found Spec version: {existing_table_spec_version}. SDK Spec version: {AthenaTableCreationSpec.SPEC_VERSION}"
            )
        else:
            logger.info(
                f"Glue table {table_spec.database}.{table_spec.table} registration needs to be updated. Dropping existing table..."
            )
            self._delete_table_if_exists(table_spec.database, table_spec.table)
            return self.create_table(table_spec)
