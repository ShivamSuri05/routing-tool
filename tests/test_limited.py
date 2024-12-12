import pandas as pd
from  functions.limited_data import get_csv_data

# Sample CSV data (this would normally be in a file, but we'll simulate it for testing)
data = """Name,Age,Gender,City
Alice,30,Female,Berlin
Bob,25,Male,Hamburg
Charlie,35,Male,Munich
David,40,Male,Hamburg
Eva,28,Female,Frankfurt"""

# Save the CSV data to a file for testing
with open("test_data.csv", "w") as file:
    file.write(data)

# Test cases
test_cases = [
    ("test_data.csv", []),  # Test case where column_list is empty (all columns)
    ("test_data.csv", ["Name", "Age"]),  # Test case where specific columns are requested
    ("test_data.csv", ["Gender", "City"])  # Test case where other specific columns are requested
]

# Run test cases
for i, (filepath, column_list) in enumerate(test_cases, 1):
    print(f"Test Case {i}:")
    print(get_csv_data(filepath, column_list))
    print("-" * 50)