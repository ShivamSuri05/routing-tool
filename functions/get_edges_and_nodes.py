import osmnx as ox

def get_data_from_place(place_name):
    """
    Fetch graph data (nodes and edges) for a specified place using osmnx.

    Parameters:
        place_name (str): Name of the place to retrieve the graph data for.

    Returns:
        dict: A dictionary containing nodes and edges data as GeoDataFrames.
            Example structure:
            {
                "edges": GeoDataFrame of edges,
                "nodes": GeoDataFrame of nodes
            }
    """
    try:
        # Retrieve the graph for the given place
        graph = ox.graph_from_place(place_name, network_type='drive')

        # Convert the graph to GeoDataFrames
        nodes, edges = ox.graph_to_gdfs(graph)

        # Create the dictionary object
        dict_object = {
            "nodes": nodes,
            "edges": edges
        }

        return dict_object
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_nearest_edge(graph, latitude, longitude, dist=False):
    nearest_edge = ox.distance.nearest_edges(graph, X=longitude, Y=latitude, return_dist=dist)
    return nearest_edge

def get_nearest_edge_data(graph, start_node, end_node):
    nearest_edge_data = graph.get_edge_data(start_node, end_node)
    return nearest_edge_data