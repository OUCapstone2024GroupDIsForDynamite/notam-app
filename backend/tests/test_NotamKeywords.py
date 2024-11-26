import unittest
import csv
import json

from objects.Notam import Notam
from utilities.NotamFetcher import NotamFetcher
from utilities.GeoUtilities import GeoUtilities
from collections import Counter

class TestNotamKeywords(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def test_frequencies(self):
        notams = self.read_notams_from_json("notam_sample.json")

        tuple_counts = Counter()
    
        ## This is the section that you would change to test different frequencies

        # Get frequencies of two keywords in a row
        for notam in notams:
            # Extract keywords from the "text" field
            text_field = getattr(notam, "text", "")
            words = text_field.split()

            for i in range (len(words) - 1):
                tuple_counts[(words[i], words[i+1])] += 1

        self.tuple_counts_to_csv(tuple_counts, "two-keywords.csv")

    def tuple_counts_to_csv(self, tuple_counts, csv_filename):
        """Writes counts and attributes to a csv file"""

        with open(csv_filename, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            # Write the header row
            writer.writerow(["Count", "Attributes"])
            
            # Write each tuple and its count
            for attributes, count in sorted(tuple_counts.items(), key=lambda x: x[1], reverse=True):
                writer.writerow([count, attributes])

        print(f"Results have been written to {csv_filename}")

    def write_notams_to_json(self, notams, json_filename):
        structured_data = [
            {
                "properties": {
                    "coreNOTAMData": {
                        "notam": notam.__dict__
                    }
                }
            }
            for notam in notams
        ]
    
        with open(json_filename, mode="w", encoding="utf-8") as jsonfile:
            json.dump(structured_data, jsonfile, indent=4)
        
        print(f"NOTAMs written to {json_filename}")
    
    def read_notams_from_json(self, json_filename):
        with open(json_filename, mode="r", encoding="utf-8") as jsonfile:
            data = json.load(jsonfile)

        # Recreate the list of NOTAM objects
        notams = [Notam(json.dumps(item)) for item in data]
        print(f"NOTAMs read from {json_filename}")
        return notams


    if __name__ == '__main__':
        unittest.main()