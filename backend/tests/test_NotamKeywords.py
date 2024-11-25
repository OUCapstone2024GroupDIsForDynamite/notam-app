import unittest
import csv

from objects.Notam import Notam
from utilities.NotamFetcher import NotamFetcher
from utilities.GeoUtilities import GeoUtilities
from collections import Counter

class TestNotamKeywords(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def test_sort_by_importance(self):
        geo_utils = GeoUtilities()

        airport_a_coor = geo_utils.geo_resolve("SAN")
        airport_b_coor = geo_utils.geo_resolve("BOS")
        flightpath_coords = geo_utils.build_flight_path(airport_a_coor, airport_b_coor)

        # Request Notams
        notam_fetcher = NotamFetcher()
        notams = notam_fetcher.fetch_by_coordinates(flightpath_coords)

        field_names = [
            "account_id", "affected_fir", "classification", "effective_start", 
            "effective_end", "icao_location", "id", "issued", "last_updated", 
            "location", "maximum_fl", "minimum_fl", "number", "purpose", 
            "scope", "series", "traffic"
        ]


        tuple_counts = Counter()
    
        for notam in notams:
            # Extract keywords from the "text" field
            text_field = getattr(notam, "text", "")
            words = text_field.split()
            
            # Count tuples of (keyword, other fields)
            for keyword in words:
                for field in field_names:
                    other_field = getattr(notam, field)
                    if str(other_field).lower() == "none":
                        continue
                    tuple_counts[(keyword, (field, other_field))] += 1

        self.display_tuple_counts_to_csv(tuple_counts, "SAN-BOS")

    def display_tuple_counts_to_csv(self, tuple_counts, csv_filename):
        """
        Writes the counts of tuples to a CSV file in the format:
        number of occurrences, attribute.

        Args:
            tuple_counts (dict): A dictionary where keys are tuples and values are counts.
            csv_filename (str): The name of the CSV file to write the results.
        """
        with open(csv_filename, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            # Write the header row
            writer.writerow(["Count", "Attributes"])
            
            # Write each tuple and its count
            for attributes, count in sorted(tuple_counts.items(), key=lambda x: x[1], reverse=True):
                writer.writerow([count, attributes])

        print(f"Results have been written to {csv_filename}")



    if __name__ == '__main__':
        unittest.main()