from typing import List

from pydantic import BaseModel


class Covariance(BaseModel):
    covariance_matrix: List[float]
