import osmnx as ox
import networkx as nx
from itertools import islice
import heapq

def filter_graph_by_height(G, vehicle_height, permissible_height=450):
    """
    Filter the graph by removing edges that do not meet the permissible height requirement.
    """
    for u, v, data in G.edges(data=True):
        if isinstance(data, dict):
            data['permissible_height'] = permissible_height

    invalid_edges = [
        (u, v) for u, v, data in G.edges(data=True)
        if isinstance(data, dict) and vehicle_height > data.get('permissible_height', float('inf'))
    ]
    G.remove_edges_from(invalid_edges)
    return G

def get_all_routes(G, start_point, end_point, k, vehicle_height, permissible_height=450):
    """
    Compute k-shortest paths using Yen's algorithm, with filtering for vehicle height.
    """
    G = filter_graph_by_height(G, vehicle_height, permissible_height)

    # Find the closest nodes to the start and end points
    start_node = ox.distance.nearest_nodes(G, X=start_point[1], Y=start_point[0])
    end_node = ox.distance.nearest_nodes(G, X=end_point[1], Y=end_point[0])

    # Find the k-shortest paths
    paths = []
    first_path = nx.shortest_path(G, source=start_node, target=end_node)
    if first_path:
        paths.append(first_path)

    for i in range(1, k):
        candidate_paths = []
        heapq.heapify(candidate_paths)

        for j in range(len(paths[i - 1]) - 1):
            G_temp = G.copy()
            G_temp.remove_edge(paths[i - 1][j], paths[i - 1][j + 1])

            try:
                path = nx.shortest_path(G_temp, source=start_node, target=end_node)
                if path not in paths:
                    heapq.heappush(candidate_paths, (len(path), path))
            except nx.NetworkXNoPath:
                continue

        if candidate_paths:
            _, new_path = heapq.heappop(candidate_paths)
            paths.append(new_path)
        else:
            break

    return paths


