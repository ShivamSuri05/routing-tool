def validate_numeric(value, allow_decimal=False, min_value=0):
    """
    Validates if a value is a positive integer or float.
    """
    try:
        num = float(value) if allow_decimal else int(value)
        return num > min_value
    except ValueError:
        return False

def validate_coordinates(value):
    """
    Validates if the input is in 'latitude,longitude' format and within valid geographic ranges.
    """
    if not isinstance(value, str) or "," not in value:
        return False

    try:
        lat, lon = map(float, value.split(","))  # Convert both parts to float
        return -90 <= lat <= 90 and -180 <= lon <= 180  # Check valid latitude & longitude ranges
    except ValueError:
        return False  # If conversion fails, input is invalid