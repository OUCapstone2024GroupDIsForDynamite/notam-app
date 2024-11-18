from typing import List
from objects.Notam import Notam
from interfaces.NotamSorter import NotamSorter

class KeywordSorter(NotamSorter):
    def __init__(self):
        pass

    def sort(self, notams: List[Notam]) -> List[Notam]:
        self.set_importance(notams)

        return sorted(
            notams,
            key=lambda notam: notam.importance
        )

    def set_importance(self, notams):
        for notam in notams:
            if " AD " in notam.text:
                notam.importance = 0
            elif " RWY " in notam.text or " TWY " in notam.text:
                notam.importance = 2
            elif " OBST " in notam.text:
                notam.importance = 3