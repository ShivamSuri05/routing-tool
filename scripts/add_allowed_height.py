import osmnx as ox
import json
import os
from functions.save_retrieve_graph import save_graph_sample, use_saved_graph_sample

def update_graph(graph, height_data, bridge_data):
    
    for key, value in height_data.items():
        # Extract nodes
        node1, node2 = map(int, key.split(','))
        
        # Determine the allowed height
        allowed_height = value['real_height'] if value['real_height'] != 10000 else value['assumed_height']
        # Update the edge property
        if graph.has_edge(node1, node2):
            graph[node1][node2][0]['allowed_height'] = allowed_height
        elif graph.has_edge(node2, node1):  # Check for reverse direction
            graph[node2][node1][0]['allowed_height'] = allowed_height

    # Update edges with bridge constraints
    for key, value in bridge_data.items():
        
        node1, node2 = map(int, key.split(','))
        # Check condition_score and load_index, and use assumed values if they are 0
        condition_score = value['condition_score'] if value['condition_score'] != 0 else value['assumed_condition_score']
        load_index = value['load_index'] if value['load_index'] != 0 else value['assumed_load_index']
        print(node1, node2)
        # Check and update the edge in the graph
        if graph.has_edge(node1, node2):
            for key, attributes in graph.get_edge_data(node1, node2).items():
                attributes['condition_score'] = condition_score
                attributes['load_index'] = load_index
        elif graph.has_edge(node2, node1):  # Check for reverse direction
            for key, attributes in graph.get_edge_data(node2, node1).items():
                attributes['condition_score'] = condition_score
                attributes['load_index'] = load_index

    BASE_PATH = os.getcwd()
    output_path = os.path.join(BASE_PATH, "routing-tool", "data", "updated_graph.graphml")
    save_graph_sample(graph, output_path)
    print("Graph updated and saved as 'updated_graph.graphml'")

if __name__ == "__main__":
    
    print("Adding height and bridge constraints in the graph")
    
    # Get the path of the current script
    script_dir = os.path.dirname(__file__)
    
    # Construct the path to the JSON file in the data folder
    height_path = os.path.join(script_dir, 'edges_and_height.json')
    bridges_path = os.path.join(script_dir, 'edges_and_bridges.json')
    graph_path = os.path.join(script_dir, 'germany.graphml')
    graph = use_saved_graph_sample(graph_path)

    # Load the JSON file
    with open(height_path, 'r') as file:
        height_path = json.load(file)

    with open(bridges_path, 'r') as file:
        bridges_path = json.load(file)


    update_graph(graph, height_path, bridges_path)
    print("Script ran successfully")
