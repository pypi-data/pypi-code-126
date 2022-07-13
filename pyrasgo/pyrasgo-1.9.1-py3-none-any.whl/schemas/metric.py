from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from datetime import datetime


class Filter(BaseModel):
    columnName: str
    operator: str
    comparisonValue: str


class Metric(BaseModel):
    id: int
    name: str
    ds_dataset_id: int = Field(alias='datasetId')
    aggregation_type: str = Field(alias='aggregationType')
    target_expression: str = Field(alias='targetExpression')
    time_grains: List[str] = Field(alias='timeGrains')
    time_dimension: str = Field(alias='timeDimension')
    dimensions: List[str]

    filters: Optional[List[Filter]]
    meta: Optional[Dict[str, str]]
    label: Optional[str]
    description: Optional[str]

    recent_values: Optional[List] = Field(alias='recentValues')
    recent_time_grain: Optional[str] = Field(alias='recentTimeGrain')
    recent_period_start: Optional[datetime] = Field(alias='recentPeriodStart')
    recent_period_end: Optional[datetime] = Field(alias='recentPeriodEnd')
