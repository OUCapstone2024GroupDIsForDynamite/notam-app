import csv

from objects.Coordinate import Coordinate
from exceptions.AirportNotFoundError import AirportNotFoundError

class GeoUtilities():
    def __init__(self):
        self.file_path = "csvs/iata-icao-lat-long.csv"
        self.iata_codes = {}  # A dictionary to store iata codes and their coordinates
        self.icao_codes = {} # A dictionary to store icao codes and their coordinates
        self.faa_codes = {} # A dictionary to store faa codes and their coordinates
        self.load_airport_data()  # Load data during initialization

    def load_airport_data(self):
        #Reads the CSV file and loads airport code and coordinate data into a dictionary.
        try:
            with open(self.file_path, mode='r', newline='', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    iata_code = row['iata'] 
                    icao_code = row['icao']
                    faa_code = row['faa']
                    lat = float(row['latitude']) 
                    long = float(row['longitude'])
                    coordinate = Coordinate(lat, long)
                    self.iata_codes[iata_code] = coordinate  # Store iata code
                    self.icao_codes[icao_code] = coordinate  # Store icao code
                    self.faa_codes[faa_code] = coordinate # store faa code
        except FileNotFoundError as e:
            print( "Couldn't find {self.file_path}. Does it exist?" )
            raise e
        except Exception as e:
            print( "An error occured while trying to load in airport data from {self.file_path}." )
            raise e
    
    def geo_resolve(self, airport):
        #Raises ValueError if airport is not a string or too long or too short
        if not isinstance(airport, str) or len(airport) not in [3,4]:
            raise ValueError(f"Airport code '{airport}' does not match the formatting requirement for airport codes.")
        
        airport = airport.upper()

        #Raises AirportNotFoundError if airport code is not in any dictionary
        if airport not in self.iata_codes and airport not in self.icao_codes and airport not in self.faa_codes:
            raise AirportNotFoundError(f"Airport code '{airport}' not found in data.")
        
        #Returns the coordinate for the airport
        return self.icao_codes.get(airport) or self.iata_codes.get(airport) or self.faa_codes.get(airport)
        
    def build_flight_path(self, coordinate_a, coordinate_b):
        #Return flight path points between two coordinates
        #Under Construction
        return [coordinate_a, coordinate_b]
