import math
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
        
        #Returns the coordinate for the airport
        return self.icao_codes.get(airport) or self.iata_codes.get(airport) or self.faa_codes.get(airport)
        
    def build_flight_path(self, coordinate_start, coordinate_end, distance_between_points = 32):
        """Return flight path points between two coordinates"""

        # Calculate number of points based on the distance between the airports
        distance_between_airports = great_circle((coordinate_start.latitude, coordinate_start.longitude), (coordinate_end.latitude, coordinate_end.longitude)).miles
        number_of_points = int(distance_between_airports / distance_between_points)

        flightpath_coordinates = []

        for i in range (number_of_points + 1):
            flightpath_coordinates.append(self.intermediate_point(coordinate_start, coordinate_end, i/number_of_points))

        return flightpath_coordinates
    
    def intermediate_point(self, coordinate_start, coordinate_end, fraction):
        """Calculate one intermediate point based on start and end coordinates and fraction along flightpath"""
        lat1 = self.deg_to_rad(coordinate_start.latitude)
        lng1 = self.deg_to_rad(coordinate_start.longitude)
        lat2 = self.deg_to_rad(coordinate_end.latitude)
        lng2 = self.deg_to_rad(coordinate_end.longitude)
        
        great_circle_angle = 2 * math.asin(
            math.sqrt(
                math.pow(math.sin((lat1 - lat2) / 2), 2) +
                math.cos(lat1) * math.cos(lat2) *
                math.pow(math.sin((lng1 - lng2) / 2), 2)
            )
        )
        
        A = math.sin((1 - fraction) * great_circle_angle) / math.sin(great_circle_angle)
        B = math.sin(fraction * great_circle_angle) / math.sin(great_circle_angle)
        
        x = A * math.cos(lat1) * math.cos(lng1) + B * math.cos(lat2) * math.cos(lng2)
        y = A * math.cos(lat1) * math.sin(lng1) + B * math.cos(lat2) * math.sin(lng2)
        z = A * math.sin(lat1) + B * math.sin(lat2)
        
        lat = math.atan2(z, math.sqrt(x**2 + y**2))
        lng = math.atan2(y, x)

        return Coordinate(self.rad_to_deg(lat), self.rad_to_deg(lng))

    def deg_to_rad(self, d):
        return d * math.pi / 180

    def rad_to_deg(self, r):
        return r * 180 / math.pi