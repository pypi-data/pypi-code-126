import csv
import sys
from typing import Tuple, Sequence, List
from oss.oss.exceptions import IsNotAColumnError

import numpy as np


def load_csv_with_headers(
    csv_path: str,
    id_field: str = "_idx",
) -> Tuple[List[dict], dict, Sequence[str]]:
    with open(csv_path) as csvfile:
        reader = csv.DictReader(csvfile)
        header = reader.fieldnames

        if header is None:
            raise ValueError("No header in the CSV file")
        if id_field not in header and id_field != "_idx":
            raise IsNotAColumnError(
                f"Error: {id_field} is not a columns of the given csv"
            )

        header = list(header)

        try:
            rows = list(reader)
        except csv.Error as e:
            sys.exit(f"file {csv_path}, line {reader.line_num}: {e}")

        if id_field != "_idx":
            header_mapping = {keyword: {"type": "keyword"} for keyword in header}
            header_mapping[id_field]["store"] = True  # type: ignore
        else:
            header.append("_idx")
            for i, row in enumerate(rows):
                row["_idx"] = str(i)
            header_mapping = {keyword: {"type": "keyword"} for keyword in header}
            header_mapping["_idx"]["store"] = True  # type: ignore

    return rows, header_mapping, header


def load_embeddings_from_numpy(embeddings_path: str) -> np.ndarray:
    embeddings = np.load(embeddings_path)
    return embeddings[embeddings.files[0]]


def load_csv_headers(
    csv_path: str,
) -> list[str]:
    with open(csv_path) as csvfile:
        reader = csv.DictReader(csvfile)
        header = reader.fieldnames

        if header is None:
            raise ValueError("No header in the CSV file")

        header = list(header)

    return header
