from abc import ABC, abstractmethod
from typing import List
from objects.Notam import Notam  

class NotamSorter(ABC):
    @abstractmethod
    def sort(self, notams: List[Notam]) -> List[Notam]:
        pass
