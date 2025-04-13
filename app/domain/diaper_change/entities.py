from datetime import datetime
from enum import Enum
from typing import Optional


class DiaperType(str, Enum):
    PEE = "pee"
    POOP = "poop"
    BOTH = "both"


class DiaperChange:
    __slots__ = (
        '_id', '_type', '_date'
    )

    def __init__(
        self,
        type: DiaperType,
        date: datetime,
        id: Optional[str] = None,
    ):
        self._id = id
        self._type = type
        self._date = date

    @property
    def type(self):
        return self._type

    @property
    def date(self):
        return self._date

    def to_dict(self):
        return {
            "id": self._id,
            "type": self._type,
            "date": self._date.isoformat() if self._date else None,
        }
