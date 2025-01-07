from functions.route_prediction import get_all_routes
from functions.route_prediction import filter_graph_by_height
from functions.get_graph import get_graph_from_place
place_name = "Frankfurt, Germany"  # Adjust to your place
G = get_graph_from_place(place_name)

# Define start and end coordinates provided by the user
start_point = (50.1322274, 8.5902786)  # Start point (lat, lon)
end_point = (50.1981735, 8.6405113)   # End point (lat, lon)

# Vehicle height provided by user (in meters)
vehicle_height = 430

# Find all simple paths in the valid graph between start and end nodes
paths = get_all_routes(G, start_point, end_point, 10, vehicle_height)
print(paths)