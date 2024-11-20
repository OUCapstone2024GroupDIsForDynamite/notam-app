import unittest

from objects.Notam import Notam
from utilities.KeywordSorter import KeywordSorter

class TestNotamSorters(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def test_sort_by_importance(self):
        # Initialize three notams
        notam1= Notam('{"properties": {"coreNOTAMData": {"notam": {"id": "Importance_3"}}}}')
        notam2= Notam('{"properties": {"coreNOTAMData": {"notam": {"id": "Importance_2"}}}}')
        notam3= Notam('{"properties": {"coreNOTAMData": {"notam": {"id": "Importance_1"}}}}')

        # Set their importance values
        notam2.importance = 1
        notam3.importance = 0

        # Add to a list in the wrong order
        notams = []
        notams.append(notam1)
        notams.append(notam2)
        notams.append(notam3)

        # Sort by importance
        notams.sort(key=lambda notam: notam.importance)

        # Check ordering
        self.assertEqual(notams[0], notam3)
        self.assertEqual(notams[1], notam2)
        self.assertEqual(notams[2], notam1)

    def test_sort_by_abbreviationsorter(self):
        AD_Notam=    Notam('{"properties": {"coreNOTAMData": {"notam": {"id": "Importance_1", "text": " AD "}}}}')
        RWY_Notam=   Notam('{"properties": {"coreNOTAMData": {"notam": {"id": "Importance_2", "text": " RWY "}}}}')
        OBST_Notam=  Notam('{"properties": {"coreNOTAMData": {"notam": {"id": "Importance_3", "text": " OBST "}}}}')
        OTHER_Notam= Notam('{"properties": {"coreNOTAMData": {"notam": {"id": "Importance_4", "text": " OTHER "}}}}')

        # Add to a list in the wrong order
        notams = []
        notams.append(OTHER_Notam)
        notams.append(OBST_Notam)
        notams.append(RWY_Notam)
        notams.append(AD_Notam)

        notams = KeywordSorter().sort(notams)

        # Check ordering
        self.assertEqual(notams[0], AD_Notam)
        self.assertEqual(notams[1], RWY_Notam)
        self.assertEqual(notams[2], OBST_Notam)
        self.assertEqual(notams[3], OTHER_Notam)

    if __name__ == '__main__':
        unittest.main()