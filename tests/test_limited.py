import pandas as pd
from  functions.limited_data import get_csv_data

# Sample CSV data 
data = """Name,Age,Gender,City
Alice,30,Female,Berlin
Bob,25,Male,Hamburg
Charlie,35,Male,Munich
David,40,Male,Hamburg
Eva,28,Female,Frankfurt"""

# Save the CSV data to a file for testing
with open("tests/test-data/test_data.csv", "w") as file:
    file.write(data)

# Test cases
test_cases = [
    ("tests/test-data/test_data.csv", ["Name", "Age"]),  
    ("tests/test-data/test_data.csv", ["Name", "Age", "Salary"]),  
    ("tests/test-data/test_data.csv", ["City", "Gender"]),
    ("tests/test-data/test_data.csv", ["Country"]),
    ("tests/test-data/test_data.csv", [])
]

# Run test cases
for i, (filepath, column_list) in enumerate(test_cases, 1):
    print(f"Test Case {i}:")
    try:
        result = get_csv_data(filepath, column_list)
        print(result)
    except ValueError as e:
        print(e)
    print("-" * 50)