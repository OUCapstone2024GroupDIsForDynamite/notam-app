import csv

from objects.Coordinate import Coordinate

class GeoUtilities():
    def __init__(self):
        self.file_path = "iata-icao-lat-long"
        self.iata_codes = {}  # A dictionary to store iata codes and their coordinates
        self.icao_codes = {} # A dictionary to store icao codes and their coordinates
        self.load_airport_data()  # Load data during initialization

    def load_airport_data(self):
        """Reads the CSV file and loads airport code and coordinate data into a dictionary."""
        try:
            with open(self.file_path, mode='r', newline='', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    iata_code = row['iata'] 
                    icao_code = row['icao']
                    lat = float(row['latitude']) 
                    long = float(row['longitude'])
                    coordinate = Coordinate(lat, long)
                    self.iata_codes[iata_code] = coordinate  # Store iata code
                    self.icao_codes[icao_code] = coordinate  # Store icao code
        except FileNotFoundError:
            print(f"Error: The file {self.file_path} does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def geo_resolve(self, airport):
        if(len(airport) == 3):
            return self.iata_codes.get(airport, None)
        if(len(airport) == 4):
            return self.icao_codes.get(airport, None)
        else:
            raise ValueError("Airport has too many or too few characters to be an iata or icao location")
        
