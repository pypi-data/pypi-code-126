from io import StringIO
from typing import Dict, Iterable

import boto3


def query_csv_s3(bucket: str, filename: str, sql_exp: str) -> StringIO:
    """function to query data in CSV in Amazon S3"""
    s3 = boto3.client("s3")
    #  query and create response
    resp = s3.select_object_content(
        Bucket=bucket,
        Key=filename,
        ExpressionType="SQL",
        Expression=sql_exp,
        InputSerialization={"CSV": {"FileHeaderInfo": "USE"}},
        OutputSerialization={"CSV": {}},
    )

    # unpack query response
    records = []
    payload: Iterable = resp["Payload"]
    for event in payload:
        if "Records" in event:
            records_: Dict[str, bytes] = event["Records"]
            payload_ = records_["Payload"]
            records.append(payload_)

    # store unpacked data as a CSV format
    file_str = "".join(req.decode("utf-8") for req in records)
    sio = StringIO(file_str)

    return sio
