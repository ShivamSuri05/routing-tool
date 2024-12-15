# Example Usage
from functions.distance_between_2_nodes import calculate_distance
coord1 = (53.29214692, 9.507763736)  # Bridge location.
coord2 = (53.2922552,	9.5085695)   # Seimens provided location near/faraway the bridge.

# Geodesic distance (straight-line)
geo_distance = calculate_distance(coord1, coord2, use_road_network=False)
print(f"Geodesic distance: {geo_distance:.2f} meters")

# Road network distance
road_distance = calculate_distance(coord1, coord2, use_road_network=True)
if road_distance is not None:
    print(f"Road network distance: {road_distance:.2f} meters")
else:
    print("No road network path found between the points.")