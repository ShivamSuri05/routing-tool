import osmnx as ox
import os

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

graph = ox.load_graphml(os.path.join(BASE_PATH, "data", "updated_graph.graphml"))

output_file = os.path.join(BASE_PATH, "data", "nodes_output.txt")

with open(output_file, "w") as file:
    for u, v, key, data in graph.edges(keys=True, data=True):
        allowed_height = data.get("allowed_height", "N/A")
        file.write(f"{u}, {v}, Allowed Height: {allowed_height}\n")