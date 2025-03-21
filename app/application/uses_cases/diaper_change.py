from domain.diaper_change.repository import DiaperChangeRepository
from domain.diaper_change.entities import DiaperChange
from datetime import datetime


class DiaperChangeUseCases(DiaperChangeRepository):
    def __init__(self, repository: DiaperChangeRepository):
        self.repository = repository

    def create(self, type: str, date: datetime):
        diaper_change = DiaperChange(type, date)
        return self.repository.create(diaper_change)

    def find(self):
        print("entrou")
        return self.repository.find()
