from pydantic import BaseModel


class WeightStatisticsElement(BaseModel):
    time: float
    weight: float
