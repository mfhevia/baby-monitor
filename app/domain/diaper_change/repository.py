from abc import ABC, abstractmethod
from .entities import DiaperChange


class DiaperChangeRepository(ABC):
    @abstractmethod
    def create(self, cambio: DiaperChange) -> DiaperChange:
        pass

    @abstractmethod
    def find(self) -> list[DiaperChange]:
        pass
