from datetime import datetime
from datetime import timedelta
from typing import Any
from typing import List
from typing import Optional

from fastapi import APIRouter
from fastapi import Body
from fastapi import Depends
from fastapi import HTTPException

from ...database import User
from ...database import Weight
from ..auth.utils import get_current_user
from .models import WeightStatisticsElement

__all__ = ("router",)

router = APIRouter()


@router.post("/add", response_model=WeightStatisticsElement)
async def add(
    user: User = Depends(get_current_user),
    weight: float = Body(...),
    timestamp: Optional[int] = Body(None),
) -> Any:
    weight = Weight(
        time=datetime.utcnow() if timestamp is None else timestamp,
        weight=weight,
        related_user=user.id,
    )
    await weight.save()
    return WeightStatisticsElement(
        time=weight.time.timestamp(), weight=weight.weight, id=weight.id
    )


@router.post("/get", response_model=List[WeightStatisticsElement])
async def get(
    user: User = Depends(get_current_user),
    count: int = Body(10),
    from_time: int = Body(None),
    to_time: Optional[int] = Body(None),
):
    if from_time is None and to_time is None:
        weights = (
            await Weight.filter(related_user=user.id).order_by("time").limit(count)
        )
    elif from_time is not None:
        from_time_datetime = datetime.utcfromtimestamp(from_time)
        to_time_datetime = (
            datetime.utcnow() if to_time is None else datetime.utcfromtimestamp(to_time)
        )
        weights = (
            await Weight.filter(
                related_user=user.id, time__range=(from_time_datetime, to_time_datetime)
            )
            .order_by("time")
            .limit(count)
        )
    else:
        raise HTTPException(status_code=400, detail="Parameter ")

    return [
        WeightStatisticsElement(
            time=element.time.timestamp(), weight=element.weight, id=element.id
        )
        for element in weights
    ]
