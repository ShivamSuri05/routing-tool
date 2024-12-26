import json
from collections import defaultdict
from functions.save_json import save_json_to_file

def combine_json_map_objects(json_files):
    merged_data = defaultdict(list)
    # Load and merge data
    for file in json_files:
        with open(file, "r") as f:
            data = json.load(f)
            for key, values in data.items():
                merged_data[key].extend(values)

    # Remove duplicate values for each key
    merged_data = {key: list(set(values)) for key, values in merged_data.items()}

    return merged_data


# Usage:
if(__name__ == "__main__"):
    print("Creating combined bund osmnx map")
    json_files = [
        'data/bund_osmnx_map_0-10000.json',
        'data/bund_osmnx_map_10000-16000.json',
        'data/bund_osmnx_map_16000-26000.json',
        'data/bund_osmnx_map_26000-33000.json',
        'data/bund_osmnx_map_33000-38887.json'
    ]
    try:
        combined_json = combine_json_map_objects(json_files)
        combined_bridge_map_filepath = f"data/bund_osmnx_map.json"
        save_json_to_file(combined_json, combined_bridge_map_filepath)
        print("Script ran successfully")
    except ValueError as e:
        print(str(e))
    
