from pydantic import BaseModel


class WeightStatisticsElement(BaseModel):
    id: int
    time: float
    weight: float
