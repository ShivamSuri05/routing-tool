import osmnx as ox

def save_graph_sample(graph, filepath):  # give the filepath in the format: filepath="./data/GraphName.graphml"
    
    try:
        # Save the graph to a graphml file
        ox.save_graphml(graph, filepath)
        print(f"Graph successfully saved to {filepath}")
        return True
    
    except Exception as e:
        print(f"Error saving graph: {e}")
        return False
    
def use_saved_graph_sample(filepath):
    try:
        # Load the saved graph from the Graphml file
        graph = ox.load_graphml(filepath)
        print(f"Graph loaded successfully from {filepath}")
        return graph
    
    except Exception as e:
        print(f"Error loading graph: {e}")
        return None 
    
