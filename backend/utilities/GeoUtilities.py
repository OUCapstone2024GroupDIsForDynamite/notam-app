from objects.Coordinate import Coordinate
from exceptions.AirportNotFoundError import AirportNotFoundError
from geopy.distance import great_circle  # Function to calculate the distances between coordinates
from utilities.GeoResolver import GeoResolver

class GeoUtilities:
    def __init__(self):
        self.file_path = "csvs/iata-icao-lat-long-extended.csv"
        self.geo_referencing = GeoResolver(self.file_path) 
    def geo_resolve(self, airport):
        try:
            return self.geo_referencing.resolve(airport)
        except ValueError as ve:
            raise ValueError(f"Invalid airport code: {airport}.") from ve
        except AirportNotFoundError:
            raise AirportNotFoundError(f"Airport code '{airport}' not found in data.")
    def build_flight_path(self, coordinate_start, coordinate_end, distance_between_points = 150):
        """Return flight path points between two coordinates"""
        """Under Construction"""
        #calculate the distance between two given airports in statue miles
        distance_between_airports = great_circle((coordinate_start.latitude, coordinate_start.longitude), (coordinate_end.latitude, coordinate_end.longitude)).miles

        #calculate total number of points
        number_of_points = int(distance_between_airports / distance_between_points)

        #find the increment values for longitude and latitude
        longitude_increment = (coordinate_end.longitude - coordinate_start.longitude) / number_of_points
        latitude_increment = (coordinate_end.latitude - coordinate_start.latitude) / number_of_points

        #calculate and add each point including the initial and final airport coordinates into a flightpath
        flightpath_coordinates = []
        for i in range(0, number_of_points):
            lat = latitude_increment * i + coordinate_start.latitude
            long = longitude_increment * i + coordinate_start.longitude
            flightpath_coordinates.append(Coordinate(lat, long))
        flightpath_coordinates.append(coordinate_end)
        return flightpath_coordinates
