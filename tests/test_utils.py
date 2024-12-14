from functions.utils import encode_coordinates,decode_coordinates

# Test cases for encode_coordinates
test_cases = [
    (53.123452,9.874523),  #should return valid output
    (53.123452,9.0),       #should return valid output
    (53.123452,9),         #should return valid output
    (53.123452,None),      #should return nothing due to None longitude
    (None,9.874523),       #should return nothing due to None latitude
    ("53.123452",9.0),     #should return nothing due to type String of latitude
    ([53.123452],9.874523) #should return nothing due to type list of latitude
]

# Run test cases for encode_coordinates
print("#Running test cases for encode_coordinates")
for i, test_case in enumerate(test_cases):
    print(f"Test Case {i+1}:")
    try:
        result = encode_coordinates(test_case[0],test_case[1])
        print(result)
    except ValueError as e:
        print(e)
    print("-" * 50)



# Test cases for decode_coordinates
test_cases = [
    "53.123452-9.874523",  #should return valid output
    "53.123452-9.0",       #should return valid output
    "53.123452-9",         #should return valid output
    "",      #should return nothing due to None longitude
    None,       #should return nothing due to None latitude
    53.123452,     #should return nothing due to type String of latitude
    [53.123452] #should return nothing due to type list of latitude
]

# Run test cases for decode_coordinates
print("Running test cases for decode_coordinates")
for i, test_case in enumerate(test_cases):
    print(f"Test Case {i+1}:")
    try:
        result = decode_coordinates(test_case)
        print(result)
    except ValueError as e:
        print(e)
    print("-" * 50)
