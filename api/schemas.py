from pydantic import BaseModel
from typing import List


class PointBase(BaseModel):
    lat: float
    lng: float


class RouteBase(BaseModel):
    id: int
    points: List[PointBase]
