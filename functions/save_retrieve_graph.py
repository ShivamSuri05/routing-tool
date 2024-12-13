import os
import osmnx as ox
import geopandas as gpd

def save_graph_sample(graph, filepath):  # give the filepath in the format: filepath="./data/GraphName.gpkg"
    if not os.path.isdir(filepath):
        print(f"Error: The directory {filepath} does not exist.")
        return False
    
    try:
        # Save the graph to a GeoPackage file
        ox.save_graph_geopackage(graph, filepath)
        print(f"Graph successfully saved to {filepath}")
        return True
    
    except Exception as e:
        print(f"Error saving graph: {e}")
        return False
    
def use_saved_graph_sample(filepath):
    try:
        # Load the saved graph from the GeoPackage file
        graph = gpd.read_file(filepath)
        print(f"Graph loaded successfully from {filepath}")
        return graph
    
    except Exception as e:
        print(f"Error loading graph: {e}")
        return None