from datetime import datetime
from enum import Enum


class DiaperType(str, Enum):
    PEE = "pee"
    POOP = "poop"
    BOTH = "both"


class DiaperChange:
    def __init__(self, type: DiaperType, date: datetime):
        self.id = None
        self.type = type
        self.date = date
