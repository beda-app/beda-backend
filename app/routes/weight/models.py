from typing import List

from pydantic import BaseModel


class WeightStatisticsElement(BaseModel):
    time: float
    weight: float


class WeightStatisticsResponse(BaseModel):
    result: List[WeightStatisticsElement]
