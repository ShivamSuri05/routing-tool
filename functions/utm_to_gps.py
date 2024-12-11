import pyproj 

def transform_UTM_to_GPS(utm_x, utm_y):
    try:
        # Check if UTM values are within valid ranges
        if not (0 <= utm_x < 1000000):
            raise ValueError(f"Invalid UTM easting: {utm_x}. It must be between 0 and 999,999 meters.")
        
        if not (0 <= utm_y < 10000000):
            raise ValueError(f"Invalid UTM northing: {utm_y}. It must be between 0 and 9,999,999 meters.")

        utm_proj = pyproj.CRS('EPSG:32632')  # UTM Zone 32N
        latlon_proj = pyproj.CRS('EPSG:4326')  # WGS84 (Latitude, Longitude)

        transformer = pyproj.Transformer.from_crs(utm_proj, latlon_proj) 
        latitude, longitude = transformer.transform(utm_x, utm_y)
        
        return {
            "gps_latitude": latitude,
            "gps_longitude": longitude
        }
    
    except ValueError as e:
        # Catch and raise error if the input is out of range
        print(f"Error: {e}")
        return None
        
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

