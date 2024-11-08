import unittest

from utilities.GeoUtilities import GeoUtilities
from objects.Coordinate import Coordinate
from exceptions.AirportNotFoundError import AirportNotFoundError

class TestGeoUtilities(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Setup for the test cases
        # Initialize GeoUtilities
        cls.geo_utilities = GeoUtilities()

    def test_load_airport_data(self):
        #Test if airport data is loaded correctly.
        self.assertIn('JFK', self.geo_utilities.iata_codes)
        self.assertIn('KLAX', self.geo_utilities.icao_codes)

    def test_get_iata_coordinate(self):
        #Test getting a coordinate for a valid IATA code. Rounded to two decimal places.
        coordinate = self.geo_utilities.geo_resolve('OKC')
        self.assertIsInstance(coordinate, Coordinate)
        self.assertEqual(round(coordinate.latitude, 2), 35.39)
        self.assertEqual(round(coordinate.longitude, 2), -97.60)

    def test_get_icao_coordinate(self):
        #Test getting a coordinate for a valid ICAO code. Rounded to two decimal places.
        coordinate = self.geo_utilities.geo_resolve('KDFW')
        self.assertIsInstance(coordinate, Coordinate)
        self.assertEqual(round(coordinate.latitude, 2), 32.9)
        self.assertEqual(round(coordinate.longitude, 2), -97.04)

    def test_get_faa_coordinate(self):
        #Test getting a coordinate for a valid ICAO code. Rounded to two decimal places.
        coordinate = self.geo_utilities.geo_resolve('1O8')
        self.assertIsInstance(coordinate, Coordinate)
        self.assertEqual(round(coordinate.latitude, 2), 34.46)
        self.assertEqual(round(coordinate.longitude, 2), -99.17)

    def test_get_coordinate_invalid(self):
        #Test getting a coordinate for an invalid code of the correct format raises AirportNotFoundError.
        with self.assertRaises(AirportNotFoundError):
            self.geo_utilities.geo_resolve('XYZ')

    def test_unformatted_airport_code(self):
        #Test getting a coordinate with an unformatted code raises ValueError if null.
        with self.assertRaises(ValueError):
            self.geo_utilities.geo_resolve(1)
        with self.assertRaises(ValueError):
            self.geo_utilities.geo_resolve('X')
    
    def test_get_coordinate_null(self):
        #Test getting a coordinate with a null address raises TypeError.
        with self.assertRaises(TypeError):
            self.geo_utilities.geo_resolve()
    
    if __name__ == '__main__':
        unittest.main()