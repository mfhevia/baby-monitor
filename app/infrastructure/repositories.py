# infrastructure/repositories.py
from domain.diaper_change.repository import DiaperChangeRepository
from domain.diaper_change.entities import DiaperChange
from .models import DiaperChangeModel
from sqlmodel import Session, select


class DiaperChangeRepositoryDB(DiaperChangeRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, diaper_change: DiaperChange):
        db_diaper_change = DiaperChangeModel(
            type=diaper_change.type,
            date=diaper_change.date
        )
        self.session.add(db_diaper_change)
        self.session.commit()
        self.session.refresh(db_diaper_change)

        return db_diaper_change

    def find(self):
        query = select(DiaperChangeModel)
        diaper_changes = self.session.exec(query).all()
        return diaper_changes
