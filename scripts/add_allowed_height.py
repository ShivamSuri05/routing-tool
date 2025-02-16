import osmnx as ox
import json
import os
from functions.save_retrieve_graph import save_graph_sample, use_saved_graph_sample


def update_graph(graph, height_data, bridge_data, condition_score_threshold, load_index_threshold):
    
    for key, value in height_data.items():
        # Extract nodes
        node1, node2 = map(int, key.split(','))
        
        # Determine the allowed height
        allowed_height = value['real_height'] if value['real_height'] != 10000 else value['assumed_height']
        assumed_flag = 0
        if(value['real_height'] == 10000 and value['assumed_height']):
            assumed_flag = 1
        # Update the edge property
        if graph.has_edge(node1, node2):
            for k in graph[node1][node2]:
                graph[node1][node2][k]['allowed_height'] = allowed_height
                if (assumed_flag == 1):
                    graph[node1][node2][k]['assumed_flag'] = 1
            #print(graph[node1][node2])
        #elif graph.has_edge(node2, node1):  # Check for reverse direction
        #    graph[node2][node1][0]['allowed_height'] = allowed_height
        #print(graph[node1][node2])
        #process.exit()

    # Update edges with bridge constraints
    for key, value in bridge_data.items():
        
        node1, node2 = map(int, key.split(','))
        # Check condition_score and load_index, and use assumed values if they are 0
        condition_score = value['condition_score'] if value['condition_score'] != 0 else value['assumed_condition_score']
        load_index = value['load_index'] if value['load_index'] != 0 else value['assumed_load_index']
        
        # Check and update the edge in the graph
        if graph.has_edge(node1, node2):
            if condition_score > condition_score_threshold or load_index > load_index_threshold:
                graph.remove_edge(node1, node2)
            else:
                for k in graph[node1][node2]:
                    graph[node1][node2][k]['condition_score'] = condition_score
                    graph[node1][node2][k]['load_index'] = load_index
    """    elif graph.has_edge(node2, node1):  # Check for reverse direction
            if condition_score > condition_score_threshold or load_index > load_index_threshold:
                graph.remove_edge(node2, node1)
            else:
                graph[node2][node1][0]['condition_score'] = condition_score
                graph[node2][node1][0]['load_index'] = load_index
    """
    
    output_path = "data/autobahns_germany_with_restrictions_v1.graphml"
    save_graph_sample(graph, output_path)
    print("Graph updated and saved in "+output_path)

if __name__ == "__main__":
    
    condition_score_threshold = 4
    load_index_threshold = 5
    
    print("Adding height and bridge constraints in the graph")
    
    height_path = 'data/edges_and_height.json'
    bridges_path = 'data/edges_and_bridges.json'
    graph_path = 'data/autobahns_germany.graphml'
    graph = use_saved_graph_sample(graph_path)

    # Load the JSON file
    with open(height_path, 'r') as file:
        height_path = json.load(file)

    with open(bridges_path, 'r') as file:
        bridges_path = json.load(file)


    update_graph(graph, height_path, bridges_path, condition_score_threshold, load_index_threshold)
    print("Script ran successfully")
