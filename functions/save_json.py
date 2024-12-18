import json

def save_json_to_file(data, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"JSON data successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving JSON data to {filename}: {e}")
