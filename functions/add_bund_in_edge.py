from functions.get_edges_and_nodes import get_nearest_edge, get_nearest_edge_data
from functions.utils import generate_nearby_points, get_assumed_nearest_edges, add_update_b_data_object

def add_bund_in_edge(graph, b_lat, b_long, condition_score, load_index, b_type, dict_object):
    nearest_edge = get_nearest_edge(graph, b_lat, b_long, True)
    if (nearest_edge[1] > 0.0002): #point does not lie on the edge
        print("Point does not lie on the edge")
        print(b_lat, b_long, nearest_edge)
        return
    
    nearest_edge = nearest_edge[0] #removing return dist column
    nearest_start_node = nearest_edge[0]
    nearest_end_node = nearest_edge[1]
    nearest_edge_data = get_nearest_edge_data(graph, nearest_start_node, nearest_end_node)
    #print("Node data1",graph.nodes[nearest_start_node])
    #print("Node data2",graph.nodes[nearest_end_node])
    oneway_flag = nearest_edge_data[0]['oneway']
    radius_to_the_point = 10 #meters
    b_data = {
        "condition_score": condition_score,
        "load_index": load_index,
        "type": b_type
    }

    if(oneway_flag==True):
        assumed_pts = generate_nearby_points(b_lat, b_long, radius_to_the_point)
        nearest_edges_list = [get_nearest_edge(graph, assumed_pt[0], assumed_pt[1]) for assumed_pt in assumed_pts]
        uniq_edges_list = set(nearest_edges_list)
        assumed_nearest_edges = get_assumed_nearest_edges(uniq_edges_list, nearest_edge)
        #print(f"For:",b_lat,b_long," Assumed edges are:")
        for assumed_edge in assumed_nearest_edges:
            assumed_nearest_start_node = assumed_edge[0]
            assumed_nearest_end_node = assumed_edge[1]
            #print("assumed_nearest_start_node:",assumed_nearest_start_node)
            #print("assumed_nearest_end_node:",assumed_nearest_end_node)
            #print("Node data1",graph.nodes[assumed_nearest_start_node])
            #print("Node data2",graph.nodes[assumed_nearest_end_node])
            add_update_b_data_object(
                assumed_nearest_start_node,
                assumed_nearest_end_node,
                b_data,
                oneway_flag,
                False,  #Assumed b_data
                dict_object
            )
        
        add_update_b_data_object(
            nearest_start_node,
            nearest_end_node,
            b_data,
            oneway_flag,
            True,  #Real Height
            dict_object
        )
    else:
        #print("Oneway is False")
        add_update_b_data_object(
            nearest_start_node,
            nearest_end_node,
            b_data,
            oneway_flag,
            True,  #Real Height
            dict_object
        )
