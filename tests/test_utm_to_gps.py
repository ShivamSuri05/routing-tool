import unittest

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../functions')))


from  ..functions.utm_to_gps import transform_UTM_to_GPS

class TestTransformUTMToGPS(unittest.TestCase):

    def test_utm_to_gps_case_1(self):
        # Test case 1
        utm_x = 744848.125
        utm_y = 5998679.5
        expected_lat = 54.0779  # Expected latitude for this UTM location 
        expected_lon = 12.7431  # Expected longitude for this UTM location 

        result = transform_UTM_to_GPS(utm_x, utm_y)
        
        # Assertions
        self.assertAlmostEqual(result['gps_latitude'], expected_lat, places=5)
        self.assertAlmostEqual(result['gps_longitude'], expected_lon, places=5)

    def test_utm_to_gps_case_2(self):
        # Test case 2
        utm_x = 0
        utm_y = 0
        expected_lat = 0 
        expected_lon = 4.511256116

        result = transform_UTM_to_GPS(utm_x, utm_y)
        
        # Assertions
        self.assertAlmostEqual(result['gps_latitude'], expected_lat, places=5)
        self.assertAlmostEqual(result['gps_longitude'], expected_lon, places=5)

    def test_invalid_utm_coordinates(self):
        # Test case 3: Invalid UTM coordinates
        utm_x = -1000000  # Invalid UTM Easting
        utm_y = -1000000  # Invalid UTM Northing

        with self.assertRaises(ValueError): 
            transform_UTM_to_GPS(utm_x, utm_y)

if __name__ == '__main__':
    unittest.main()

