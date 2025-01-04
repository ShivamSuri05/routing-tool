import osmnx as ox
import json
import os
from functions.save_retrieve_graph import save_graph_sample, use_saved_graph_sample

def update_graph_with_height(graph_path, json_data, output_path):
    
    graph = use_saved_graph_sample(graph_path)
    
    for key, value in json_data.items():
        # Extract nodes
        node1, node2 = map(int, key.split(','))
        
        # Determine the allowed height
        allowed_height = value['real_height'] if value['real_height'] != 10000 else value['assumed_height']
        # Update the edge property
        if graph.has_edge(node1, node2):
            graph[node1][node2][0]['allowed_height'] = allowed_height
        elif graph.has_edge(node2, node1):  # Check for reverse direction
            graph[node2][node1][0]['allowed_height'] = allowed_height

    
    # Save the updated graph
    save_graph_sample(graph, output_path)

# Define the paths
script_dir = os.path.dirname(__file__)
    
# Construct the path to the JSON file in the data folder
json_path = os.path.join(script_dir, 'edges_and_height.json')

# Load the JSON file
with open(json_path, 'r') as file:
    json_data = json.load(file)

BASE_PATH = os.getcwd()
graph_path = os.path.join(BASE_PATH, "germany.graphml")
output_path = os.path.join(BASE_PATH, "updated_graph.graphml")


update_graph_with_height(graph_path, json_data, output_path)

