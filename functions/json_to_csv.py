import json  
import csv

def json_to_csv(json_file_path, csv_file_path):
   
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    keys = list(data.keys())
    values = list(data.values())
    field_names = ['key']
    field_names += list(values[0].keys())

    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        for k,v in zip(keys, values):
            v[field_names[0]] = k
            writer.writerow(v)


if __name__ == '__main__':
    json_file_path = r'D:\Sparsha\Fishing\routing-tool\tests\test-data\Example.json'  # Path to JSON file
    csv_file_path = r'D:\Sparsha\Fishing\routing-tool\tests\test-dataoutput.csv'   # Path to save the CSV file
    json_to_csv(json_file_path, csv_file_path)