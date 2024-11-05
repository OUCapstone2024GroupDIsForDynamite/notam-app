from typing import List
from objects.Notam import Notam
from interfaces.NotamSorter import NotamSorter

class DummySorter(NotamSorter):
    def __init__(self):
        pass

    def sort(self, notams: List[Notam]) -> List[Notam]:
        criteria = 'id'  # Hard Coded for now, UI will determine sorting criteria in the future

        # Validate the sorting criteria against Notam attributes
        valid_criteria = [
            'account_id', 'affected_fir', 'classification', 
            'effective_start', 'effective_end', 'icao_location', 
            'id', 'issued', 'last_updated', 'location', 
            'maximum_fl', 'minimum_fl', 'number', 'purpose', 
            'scope', 'selection_code', 'series', 
            'traffic', 'type', 'text'
        ]

        if criteria not in valid_criteria:
            raise ValueError(f"Invalid sorting criteria. Choose from: {valid_criteria}")

        # Sort the NOTAMs based on the specified criteria, with None values placed at the end
        return sorted(
            notams,
            key=lambda notam: (getattr(notam, criteria) is None, getattr(notam, criteria))
        )
