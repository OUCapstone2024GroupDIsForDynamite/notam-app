import unittest

from objects.Notam import Notam

class TestGeoUtilities(unittest.TestCase):
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

    if __name__ == '__main__':
        unittest.main()