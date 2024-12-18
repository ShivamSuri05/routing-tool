import osmnx as ox
import os
import networkx as nx
from functions.save_retrieve_graph import save_graph_sample, use_saved_graph_sample
from functions.get_graph import get_graph_from_place

# Define the place name and the file path
place_name = "Nieder-Weisel, Germany"
G = get_graph_from_place(place_name)

valid_filepath = "test_directory/test.graphml"
os.makedirs(os.path.dirname(valid_filepath), exist_ok=True)

try:
    # Test 1: Save the graph to a valid directory
    save_result = save_graph_sample(G, valid_filepath)
    
    # Test 2: Load the graph from the valid file
    loaded_graph = use_saved_graph_sample(valid_filepath)
    if loaded_graph:
        ox.plot_graph(loaded_graph)
    else:
        print("Graph could not be loaded.")
    
finally:
    # Clean up: Not Delete the test file if it exists
    if os.path.exists(valid_filepath):
        #os.remove(valid_filepath)
        print(f"File {valid_filepath} has not been deleted for safety.")
    else:
        print(f"File {valid_filepath} does not exist.")
