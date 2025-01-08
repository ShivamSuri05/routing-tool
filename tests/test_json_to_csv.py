import pandas as pd
from functions.json_to_csv import json_to_csv

if __name__ == '__main__':
    json_file_path = r'D:\Sparsha\Fishing\routing-tool\tests\test-data\Example.json'  # Path to JSON file
    csv_file_path = r'D:\Sparsha\Fishing\routing-tool\tests\test-dataoutput.csv'   # Path to save the CSV file
    json_to_csv(json_file_path, csv_file_path)