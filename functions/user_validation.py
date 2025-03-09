def validate_numeric(value, allow_decimal=False, min_value=0):
    """
    Validates if a value is a positive integer or float.
    Returns False for invalid values and True for valid ones.
    """
    try:
        # Convert to float if decimals are allowed, otherwise to int
        num = float(value) if allow_decimal else int(value)

        # Check if the value is negative
        if num < 0:
            return False  # Return False for negative values

        # Return True if the value is greater than the minimum value
        return num > min_value

    except ValueError:
        return False  # Return False for invalid input (e.g., non-numeric)

def validate_coordinates(value):
    """
    Validates if the input is in 'latitude,longitude' format and within valid geographic ranges.
    """
    if not isinstance(value, str) or " " not in value:
        return False
    try:
        lat, lon = map(float, value.split(" "))
        return -90 <= lat <= 90 and -180 <= lon <= 180
    except ValueError:
        return False

def validate_integer(value, min_value=1):
    """
    Validates if a value is a positive integer (number of paths can't be a float).
    """
    try:
        num = int(value)
        return num >= min_value
    except ValueError:
        return False