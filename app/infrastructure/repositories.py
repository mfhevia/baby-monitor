from typing import List
from domain.diaper_change.repository import DiaperChangeRepository
from domain.diaper_change.entities import DiaperChange
from infrastructure.models import DiaperChangeModel
from sqlmodel import Session, select


class DiaperChangeRepositoryDB(DiaperChangeRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, diaper_change: DiaperChange) -> DiaperChange:
        db_diaper_change = DiaperChangeModel(
            type=diaper_change.type,
            date=diaper_change.date
        )
        self.session.add(db_diaper_change)
        self.session.commit()
        self.session.refresh(db_diaper_change)

        return DiaperChange(
            id=str(db_diaper_change.id),
            type=db_diaper_change.type,
            date=db_diaper_change.date
        )

    def find(self) -> List[DiaperChange]:
        query = select(DiaperChangeModel).where()
        db_diaper_changes = self.session.exec(query).all()
        return [DiaperChange(
            id=str(db_diaper_change.id),
            type=db_diaper_change.type,
            date=db_diaper_change.date
        ) for db_diaper_change in db_diaper_changes]
