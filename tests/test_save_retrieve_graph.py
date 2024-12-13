import osmnx as ox
import os
import networkx as nx
from functions.save_retrieve_graph import save_graph_sample, use_saved_graph_sample

# Define the place name and the file path
place_name = "Nieder-Weisel, Germany"
G = ox.graph_from_place(place_name, network_type="drive")

valid_filepath = "valid_directory/test.gpkg"
os.makedirs(os.path.dirname(valid_filepath), exist_ok=True)

try:
    # Test 1: Save the graph to a valid directory
    print("Test 1: Saving graph to a valid directory")
    save_result = save_graph_sample(G, valid_filepath)
    if save_result:
        print(f"Graph saved to {valid_filepath}")
    else:
        print("Graph not saved.")
    
    # Test 2: Load the graph from the valid file
    print("\nTest 2: Loading graph from a valid file")
    loaded_graph = use_saved_graph_sample(valid_filepath)
    if loaded_graph:
        print("Graph loaded successfully.")
    else:
        print("Graph could not be loaded.")
    
finally:
    # Clean up: Delete the test file if it exists
    if os.path.exists(valid_filepath):
        os.remove(valid_filepath)
        print(f"File {valid_filepath} has been deleted.")
    else:
        print(f"File {valid_filepath} does not exist.")
