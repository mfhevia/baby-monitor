# infrastructure/repositories.py
from domain.diaper_change.repository import DiaperChangeRepository
from domain.diaper_change.entities import DiaperChange


class DiaperChangeRepositoryDB(DiaperChangeRepository):
    def __init__(self):
        self.changes = []
        self.count = 0

    def create(self, diaperChange: DiaperChange):
        diaperChange.id = self.count
        self.count += 1
        self.changes.append(diaperChange)
        return diaperChange
        # self.db_connection.insert_one(diaperChange.__dict__)

    def find(self):
        return self.changes
