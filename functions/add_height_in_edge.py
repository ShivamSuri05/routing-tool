from functions.get_edges_and_nodes import get_nearest_edge, get_nearest_edge_data
from functions.utils import generate_nearby_points, get_assumed_nearest_edges, add_update_json_object, add_to_map, update_to_map

def add_height_in_edge(graph, s_lat, s_long, height, dict_object, si_os_map):
    nearest_edge = get_nearest_edge(graph, s_lat, s_long)
    nearest_start_node = nearest_edge[0]
    nearest_end_node = nearest_edge[1]
    nearest_edge_data = get_nearest_edge_data(graph, nearest_start_node, nearest_end_node)
    #print("Node data1",graph.nodes[nearest_start_node])
    #print("Node data2",graph.nodes[nearest_end_node])
    oneway_flag = nearest_edge_data[0]['oneway']
    radius_to_the_point = 15 #meters

    add_to_map(s_lat, s_long, nearest_start_node, nearest_end_node, si_os_map)

    if(oneway_flag==True):
        assumed_pts = generate_nearby_points(s_lat, s_long, radius_to_the_point)
        nearest_edges_list = [get_nearest_edge(graph, assumed_pt[0], assumed_pt[1]) for assumed_pt in assumed_pts]
        uniq_edges_list = set(nearest_edges_list)
        assumed_nearest_edges = get_assumed_nearest_edges(uniq_edges_list, nearest_edge)
        #print(f"For:",s_lat,s_long," Assumed edges are:")
        for assumed_edge in assumed_nearest_edges:
            assumed_nearest_start_node = assumed_edge[0]
            assumed_nearest_end_node = assumed_edge[1]
            #print("assumed_nearest_start_node:",assumed_nearest_start_node)
            #print("assumed_nearest_end_node:",assumed_nearest_end_node)
            #print("Node data1",graph.nodes[assumed_nearest_start_node])
            #print("Node data2",graph.nodes[assumed_nearest_end_node])
            update_to_map(s_lat, s_long, assumed_nearest_start_node, assumed_nearest_end_node, si_os_map)
            add_update_json_object(
                assumed_nearest_start_node,
                assumed_nearest_end_node,
                height,
                oneway_flag,
                False,    #Assumed Height
                dict_object
            )
        
        add_update_json_object(
                nearest_start_node,
                nearest_end_node,
                height,
                oneway_flag,
                True,  #Real Height
                dict_object
            )
        
    else:
        #save dict object
        #print("Oneway is False")
        add_update_json_object(
            nearest_start_node,
            nearest_end_node,
            height,
            oneway_flag,
            True,  #Real Height
            dict_object
        )
