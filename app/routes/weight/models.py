from typing import List

from pydantic import BaseModel


class WeightStatisticsElement(BaseModel):
    id: int
    time: float
    weight: float


class GetWeightsResponse(BaseModel):
    weights: List[WeightStatisticsElement]
    count: int
