

import boto3
import io
import pandas as pd
import datetime
import logging
import numpy as np
from io import BytesIO
from time import time
import psutil
import sys
import os
import shutil
from pyspark.sql import SparkSession
from pyspark.sql.functions import split, explode, col, udf, lit
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, BinaryType, LongType, BooleanType, TimestampType, DoubleType
from pyspark.sql import DataFrame as SparkDataFrame


class tfClient():
    def __init__(self, file, s3_client, s3_bucket, s3_target_prefix, partition_start, **kwargs):
        self.file = file
        self.file_name = file.split('/')[-1].split('.')[0]
        self.s3_bucket = s3_bucket
        self.s3_prefix = s3_target_prefix
        self.partition_date = partition_start
        self.s3_client = s3_client
        self.spark = self._create_spark_session()
        return

    def read_parquet(self, **kwargs) -> pd.DataFrame:
        return pd.read_parquet(self.file, **kwargs)

    def read_csv(self, **kwargs) -> pd.DataFrame:
        return pd.read_csv(self.file, **kwargs)

    # doesnt seem faster than reading via pd.read_parquet. However, might be useful if you need to read file twice with different config
    def read_s3_object_to_memory(self, file_name):
        bucket, key = file_name.split('//')[1].split('/',1)
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(bucket)
        object = bucket.Object(key)
        file_stream = io.BytesIO()
        object.download_fileobj(file_stream)
        # https://stackoverflow.com/questions/61690731/pandas-read-csv-from-bytesio
        file_stream.seek(0)
        return file_stream

    def format_timestamps(self, df:pd.DataFrame) -> pd.DataFrame:
        datetime_df = df.select_dtypes(include="datetime")
        datetime_cols = datetime_df.columns
        # replace cogenius NULL with datetimelike string in order to convert via .dt accessor
        if datetime_cols:
            df[datetime_cols] = df[datetime_cols].replace({None: '2000-01-01 00:00:00.000'})
            df[datetime_cols] = df[datetime_cols].apply(pd.to_datetime, format='%Y-%m-%d %H:%M:%S', errors='coerce')
        return df

    # ensure consistency with parser.meta_cols, parser.spark_meta_cols
    def add_metadata(self, df:pd.DataFrame) -> pd.DataFrame:
        df['META_file_name'] = self.file_name
        df['META_partition_date'] = self.partition_date
        df['META_partition_date'] = df['META_partition_date'].apply(pd.to_datetime, format='%Y-%m-%d', errors='coerce')
        df['META_processing_date_utc'] = datetime.datetime.utcnow()
        df['META_processing_date_utc'] = df['META_processing_date_utc'].apply(pd.to_datetime, format='%Y-%m-%d %H:%M:%S', errors='coerce')
        return df

    def write_parquet(self, df: pd.DataFrame) -> None:
        parquet_buffer = BytesIO()
        df.to_parquet(parquet_buffer, index=False, allow_truncated_timestamps=True)
        s3 = boto3.resource('s3')
        timestamp = round(time(), 4)
        s3_key = f"{self.s3_prefix}{timestamp}_{self.file_name}.parquet"
        s3.Object(self.s3_bucket, s3_key).put(Body=parquet_buffer.getvalue())
        logging.info(f'Stored {s3_key} on s3 {self.s3_bucket}')
        del df
        return

    def _create_spark_session(self, loglevel = "ERROR"):
        nbr_cores = self._get_nbr_cores()
        spark = SparkSession.builder.master(f"local[{nbr_cores}]") \
                    .appName(f'Spark_{self.s3_prefix}') \
                    .getOrCreate()
        spark.sparkContext.setLogLevel(loglevel)
        return spark

    def _get_nbr_cores(self):
       return psutil.cpu_count(logical = False)

    def apply_spark_schema(self, df:pd.DataFrame, schema) -> SparkDataFrame:
        spark_df = self.spark.createDataFrame(df, schema = schema)
        return spark_df

    def spark_to_parquet(self, spark_df):
        timestamp = round(time(), 4)
        local_path= f"{self.s3_prefix}{timestamp}_{self.file_name}.parquet"
        local_path =  f'./data'
        shutil.rmtree(local_path)
        try:
            spark_df.write.mode('overwrite').parquet(local_path)
            for file in os.listdir(local_path):
                local_file = f'{local_path}/{file}'
                if '.crc' in file:
                    os.remove(local_file)
                    continue
                elif 'SUCCESS' in file:
                    os.remove(local_file)
                    continue
                else:
                    self.s3_client.upload_local_file(local_file, self.s3_prefix)
                    os.remove(local_file)
            os.rmdir(local_path)
            logging.info(f'Succesfully wrote {self.s3_prefix}')
        except Exception as e:
            logging.error(f'Issue creating parquet file: {s3_prefix}. Exiting...')
            logging.error(e)
            sys.exit(1)
        return 
        