# Test case 1: Valid UTM coordinates within the range for UTM Zone 32N
from functions.utm_to_gps import transform_UTM_to_GPS


utm_x_1 = 500000  # Easting within valid range
utm_y_1 = 4649776  # Northing within valid range

result_1 = transform_UTM_to_GPS(utm_x_1, utm_y_1)
print(f"Test Case 1 - Valid UTM coordinates: {result_1}")

# Test case 2: Invalid UTM easting (outside valid range)
utm_x_2 = -100  # Invalid Easting (negative value)
utm_y_2 = 4649776  # Northing within valid range

result_2 = transform_UTM_to_GPS(utm_x_2, utm_y_2)
print(f"Test Case 2 - Invalid UTM easting: {result_2}")

# Test case 3: Invalid UTM northing (outside valid range)
utm_x_3 = 500000  # Easting within valid range
utm_y_3 = 10000000  # Invalid Northing (exactly at the upper limit, should fail)

result_3 = transform_UTM_to_GPS(utm_x_3, utm_y_3)
print(f"Test Case 3 - Invalid UTM northing: {result_3}")


