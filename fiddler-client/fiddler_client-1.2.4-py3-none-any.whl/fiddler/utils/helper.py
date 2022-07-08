import re
from typing import Union, Optional

import pandas as pd

from ..core_objects import BatchPublishType


def infer_data_source(source: Union[str, pd.DataFrame]):
    """
    Attempts to infer the type of object based on type
    """
    if isinstance(source, pd.DataFrame):
        source_type = BatchPublishType.DATAFRAME
    elif isinstance(source, str):
        if re.match(r"((s3-|s3\.)?(.*)\.amazonaws\.com|^s3://)", source):
            source_type = BatchPublishType.AWS_S3
        elif re.match(r"((gs-|gs\.)?(.*)\.cloud.google\.com|^gs://)", source):
            source_type = BatchPublishType.GCP_STORAGE
        else:
            source_type = BatchPublishType.LOCAL_DISK
    else:
        raise ValueError("Unable to infer BatchPublishType")

    return source_type


def convert_flat_csv_data_to_grouped(
    input_data: pd.DataFrame, group_by_col: str, output_path: Optional[str] = None
) -> pd.DataFrame:
    """
    input_data: The dataframe with flat data.
    group_by_col: The column to group the data by.
    output_path: Optional argument, the path to write the grouped data to. If not specified, data won't be written anywhere.
    """
    grouped_df = input_data.groupby(by=group_by_col, sort=False)
    grouped_df = grouped_df.aggregate(lambda x: x.tolist())

    if output_path is not None:
        grouped_df.to_csv(output_path)

    return grouped_df
