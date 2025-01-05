import json
from collections import defaultdict
from functions.save_json import save_json_to_file

def combine_json_objects(json_files):
    combined_data = defaultdict(lambda: {
        "condition_score": float('-inf'),
        "load_index": float('-inf'),
        "assumed_condition_score": float('-inf'),
        "assumed_load_index": float('-inf'),
        "all_condition_score": [],
        "all_load_index": [],
        "all_type": [],
        "oneway": None
    })

    for file_path in json_files:
        with open(file_path, 'r') as f:
            data = json.load(f)

            for key, value in data.items():
                # Update max values
                combined_data[key]["condition_score"] = max(combined_data[key]["condition_score"], value["condition_score"])
                combined_data[key]["load_index"] = max(combined_data[key]["load_index"], value["load_index"])
                combined_data[key]["assumed_condition_score"] = max(combined_data[key]["assumed_condition_score"], value["assumed_condition_score"])
                combined_data[key]["assumed_load_index"] = max(combined_data[key]["assumed_load_index"], value["assumed_load_index"])

                # Append lists
                combined_data[key]["all_condition_score"].extend(value["all_condition_score"])
                combined_data[key]["all_load_index"].extend(value["all_load_index"])
                combined_data[key]["all_type"].extend(value["all_type"])

                # Ensure oneway is consistent
                if combined_data[key]["oneway"] is None:
                    combined_data[key]["oneway"] = value["oneway"]
                elif combined_data[key]["oneway"] != value["oneway"]:
                    raise ValueError(f"Inconsistent 'oneway' values for key: {key}")
                else:
                    print("Another Entry found for ", key)

    return combined_data

# Usage:
if(__name__ == "__main__"):
    print("Creating combined bund edge data for the dataset")
    json_files = [
        'data/edges_and_bridges_0-10000.json',
        'data/edges_and_bridges_10000-16000.json',
        'data/edges_and_bridges_16000-26000.json',
        'data/edges_and_bridges_26000-33000.json',
        'data/edges_and_bridges_33000-38887.json'
    ]
    try:
        combined_json = combine_json_objects(json_files)
        combined_bridge_data_filepath = f"data/edges_and_bridges.json"
        save_json_to_file(combined_json, combined_bridge_data_filepath)
        print("Script ran successfully")
    except ValueError as e:
        print(str(e))
    
