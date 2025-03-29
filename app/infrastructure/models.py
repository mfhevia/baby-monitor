from sqlmodel import Field, SQLModel
from datetime import datetime
from domain.diaper_change.entities import DiaperType
import uuid


class DiaperChangeModel(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    type: DiaperType
    date: datetime = Field(default_factory=datetime.now)
