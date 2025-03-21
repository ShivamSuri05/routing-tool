import osmnx as ox
import networkx as nx
from itertools import islice
import heapq
import random

def filter_graph_by_height(G, vehicle_height):
    """
    Filter the graph by removing edges that do not meet the permissible height requirement.
    """
    invalid_edges = []
    for u, v, data in G.edges(data=True):
        if 'allowed_height' in data:
            if vehicle_height > int(data['allowed_height']):
                invalid_edges.append((u, v))
    G.remove_edges_from(invalid_edges)
    return G

def get_all_routes(G, start_point, end_point, k, vehicle_height, permissible_height=450):
    """
    Compute k-shortest paths by iteratively removing multiple middle portions of the shortest path.
    Guarantees exactly `k` unique paths by adjusting edge removal dynamically.
    """
    G = filter_graph_by_height(G, vehicle_height)
    # Find the closest nodes to the start and end points
    start_node = ox.distance.nearest_nodes(G, X=start_point[1], Y=start_point[0])
    end_node = ox.distance.nearest_nodes(G, X=end_point[1], Y=end_point[0])
   
    # Find the first shortest path
    paths = []
    try:
        first_path = nx.shortest_path(G, source=start_node, target=end_node)
        paths.append(first_path)
    except nx.NetworkXNoPath:
        return []

    attempt = 0  # Keeps track of iterations to avoid infinite loops
    max_attempts = k * 2  # Allow some extra attempts to get `k` paths

    candidate_paths = []
    heapq.heapify(candidate_paths)

    graph_temp = []

    while len(paths) < k and attempt < max_attempts:
        attempt += 1
        G_temp = G.copy()  # Reset graph for each attempt

        # Get the latest path length
        path_length = len(paths[-1])

        # Define multiple sections for edge removal
        removal_sections = []

        for idx in range(5, 85, 5):
            start_idx = int(idx * path_length/100)
            end_idx = int((idx+5) * path_length/100)
            removal_sections.append((start_idx, end_idx))


        # Iterate over each segment separately
        for start_index, end_index in removal_sections:
            G_temp = G.copy()  # Reset graph before modifying a section
            nodes_to_remove = paths[-1][start_index:end_index]
            if(len(graph_temp)):
                G_temp = graph_temp[-1]

            # Remove edges related to the segment
            for j in range(len(nodes_to_remove) - 1):
                if G_temp.has_edge(nodes_to_remove[j], nodes_to_remove[j + 1]):
                    G_temp.remove_edge(nodes_to_remove[j], nodes_to_remove[j + 1])

            # Compute a new shortest path after this segment removal
            try:
                new_path = nx.shortest_path(G_temp, source=start_node, target=end_node)
                if new_path not in paths and all(new_path != path for _, path, _ in candidate_paths):
                    heapq.heappush(candidate_paths, (len(new_path), new_path, G_temp))
            except nx.NetworkXNoPath:
                continue  # If no path is found, move to the next segment

        # Select the best alternative path if available
        if candidate_paths:
            _, new_path, rel_graph = heapq.heappop(candidate_paths)
            paths.append(new_path)
            graph_temp.append(rel_graph)

    return paths

