from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from typing import Optional


class DiaperType(str, Enum):
    PEE = "pee"
    POOP = "poop"
    BOTH = "both"


class DiaperChangeCreateSchema(BaseModel):
    type: DiaperType
    date: Optional[datetime] = None


class DiaperChangeResponseDataSchema(BaseModel):
    id: str
    type: DiaperType
    date: datetime


class DiaperChangeSingleResponseSchema(BaseModel):
    data: DiaperChangeResponseDataSchema


class DiaperChangeListResponseSchema(BaseModel):
    data: list[DiaperChangeResponseDataSchema]
