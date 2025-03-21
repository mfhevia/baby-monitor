from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from typing import Optional


class DiaperType(str, Enum):
    PEE = "pee"
    POOP = "poop"
    BOTH = "both"


class DiaperChangeSchema(BaseModel):
    type: DiaperType
    date: Optional[datetime] = None
