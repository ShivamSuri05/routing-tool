from functions.get_edges_and_nodes import get_nearest_edge_data
from functions.save_retrieve_graph import use_saved_graph_sample

valid_filepath = "data/autobahns_germany.graphml"
loaded_graph = use_saved_graph_sample(valid_filepath)
node1 = 480764
node2 = 3075304544
data = get_nearest_edge_data(loaded_graph, node1, node2)
print(f"Edge Data for {node1} and {node2}")
print(data)

linestring_wkt = str(data[0]['geometry'])
coordinates_str = linestring_wkt.replace("LINESTRING (", "").replace(")", "")
coordinate_pairs = coordinates_str.split(", ")
coordinates_list = [tuple(map(float, coord.split())) for coord in coordinate_pairs]
coor_rev = []
for coor in coordinates_list:
    tup = (coor[1],coor[0])
    coor_rev.append(tup)

print("Geometry coordinates are::")
print(coor_rev)