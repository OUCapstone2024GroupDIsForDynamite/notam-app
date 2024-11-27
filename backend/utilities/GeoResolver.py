import csv
from objects.Coordinate import Coordinate
from exceptions.AirportNotFoundError import AirportNotFoundError

class GeoResolver:
    def __init__(self, file_path):
        self.file_path = file_path
        self.iata_codes = {}
        self.faa_codes = {} 
        self.load_airport_data() 

    def load_airport_data(self):
        try:
            with open(self.file_path, mode='r', encoding='utf-8-sig') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    # Extract codes and coordinates
                    iata = row.get('iata', '').strip()
                    faa = row.get('faa', '').strip()
                    latitude = float(row.get('latitude', 0))
                    longitude = float(row.get('longitude', 0))
                    coordinate = Coordinate(latitude, longitude)

                    # Populate dictionaries
                    if iata:
                        self.iata_codes[iata] = coordinate
                    if faa:
                        self.faa_codes[faa] = coordinate

        except FileNotFoundError as e:
            raise FileNotFoundError(f"Couldn't find {self.file_path}. Does it exist?") from e
        except Exception as e:
            raise Exception(f"An error occurred while loading airport data: {str(e)}") from e

    def resolve(self, airport):
        if not isinstance(airport, str) or len(airport) not in [3, 4]:
            raise ValueError(f"Invalid airport code: '{airport}'")

        airport = airport.upper()

        # Attempt to resolve IATA code first
        if airport in self.iata_codes:
            return self.iata_codes[airport]

        # Fall back to FAA code if IATA not found
        if airport in self.faa_codes:
            return self.faa_codes[airport]

        # Raise error if neither is found
        raise AirportNotFoundError(f"Airport code '{airport}' not found in IATA or FAA data.")
