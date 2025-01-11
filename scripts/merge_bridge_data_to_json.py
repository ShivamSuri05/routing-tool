import pandas as pd
import json
import os

def update_edges_from_json(input_file, json_file, output_file):
    """
    Updates a CSV/Excel file with a new column for 'edges' by matching latitude and longitude
    with keys in a JSON file.

    Args:
        input_file (str): Path to the input CSV/Excel file.
        json_file (str): Path to the JSON file containing edge_list values.
        output_file (str): Path to save the updated CSV/Excel file.
    """
    # Load the dataset (CSV or Excel) into a pandas DataFrame
    if input_file.endswith('.csv'):
        file_dataset = pd.read_csv(input_file)
    elif input_file.endswith('.xlsx'):
        file_dataset = pd.read_excel(input_file)
    else:
        raise ValueError("Unsupported file format. Please provide a CSV or Excel file.")

    # Load edge data from the JSON file
    with open(json_file, 'r') as f:
        edge_data = json.load(f)

    # Ensure 'edges' column exists in the dataset
    if 'edges' not in file_dataset.columns:
        file_dataset['edges'] = None

    # Iterate through rows in the dataset
    for index, row in file_dataset.iterrows():
        lat, long = row['latitude'], row['longitude']
        key = f"{lat},{long}"  # Format the key for the JSON file

        # Check if the key exists in the JSON
        if key in edge_data:
            edge_list = edge_data[key]

            # Append edges to the column
            if pd.isna(file_dataset.at[index, 'edges']):
                file_dataset.at[index, 'edges'] = edge_list
            else:
                if isinstance(file_dataset.at[index, 'edges'], list):
                    file_dataset.at[index, 'edges'].extend(edge_list)
                else:
                    file_dataset.at[index, 'edges'] = [file_dataset.at[index, 'edges']] + edge_list

    # Save the updated dataset back to the file
    if output_file.endswith('.csv'):
        file_dataset.to_csv(output_file, index=False)
    elif output_file.endswith('.xlsx'):
        file_dataset.to_excel(output_file, index=False)
    else:
        raise ValueError("Unsupported file format. Please provide a CSV or Excel file.")

    print(f"Updated file saved to {output_file}")

if(__name__ == "__main__"):
    print("merging edge data with latitude and longitude for the bridge dataset")
    BASE_PATH = "C:/Users/Admin/Desktop/Fishing_for_Experience/My_tasks"
    print(BASE_PATH)
    bridge_data = os.path.join(BASE_PATH, "routing-tool", "data", "bridge_data.xlsx")
    bund_osmnx_map = os.path.join(BASE_PATH, "routing-tool", "data", "bund_osmnx_map.json")
    merged_lat_long_with_edges = os.path.join(BASE_PATH, "routing-tool", "data", "merged_lat_long_with_edges.xlsx")
    #os.makedirs(merged_lat_long_with_edges, exist_ok=True)
    update_edges_from_json(bridge_data, bund_osmnx_map, merged_lat_long_with_edges)
    print("Script ran successfully")