import math

def encode_coordinates(latitude, longitude):
    if(latitude==None or longitude==None):
        print("Please provide both latitude and longitude values")
        return
    if(type(latitude)==float and type(latitude)==float):
        return str(latitude)+"-"+str(longitude)
    else:
        print("Invalid Data type::Supported Data types=float")
        return

def decode_coordinates(string):
    if(string==None or string==""):
        print("The String is empty")
        return
    if(type(string)==str):
        return list(map(float,string.split('-')))
    else:
        print("Invalid Data type::Supported Data type=string")
        return

def generate_nearby_points(latitude, longitude, distance_m):
  meters_per_degree_lat = 111320
  meters_per_degree_lon = 111320 * math.cos(math.radians(latitude))

  delta_lat = distance_m / meters_per_degree_lat
  delta_lon = distance_m / meters_per_degree_lon

  return [(latitude + delta_lat, longitude), (latitude - delta_lat, longitude), (latitude, longitude + delta_lon),(latitude, longitude - delta_lon)]

  def get_unique_nearest_edges(edge_list):
    return set(edge_list)

def get_assumed_nearest_edges(uniq_edge_list, edge):
    return list(uniq_edge_list-set([edge]))

def add_update_json_object(start_node, end_node, height, oneway_flag, real_flag, dict_object):
    key = f"{start_node},{end_node}"
    if key not in dict_object:
        dict_object[key] = {
            "real_height": 10000,
            "assumed_height": 10000,
            "all_heights": [],
            "oneway": oneway_flag
        }

    dict_object[key]["all_heights"].append(height)

    if(real_flag == True):
        dict_object[key]["real_height"] = min(height, dict_object[key]["real_height"])
    else:
        dict_object[key]["assumed_height"] = min(height, dict_object[key]["assumed_height"])

def add_update_b_data_object(start_node, end_node, b_data, oneway_flag, real_flag, dict_object):
    key = f"{start_node},{end_node}"
    if key not in dict_object:
        dict_object[key] = {
            "condition_score": 0,
            "load_index": 10,
            "assumed_condition_score": 0,
            "assumed_load_index": 10,
            "all_condition_score": [],
            "all_load_index": [],
            "all_type": [],
            "oneway": oneway_flag
        }

    dict_object[key]["all_condition_score"].append(b_data["condition_score"])
    dict_object[key]["all_load_index"].append(b_data["load_index"])
    dict_object[key]["all_type"].append(b_data["type"])

    if(real_flag == True):
        dict_object[key]["condition_score"] = max(b_data["condition_score"], dict_object[key]["condition_score"])
        dict_object[key]["load_index"] = min(b_data["load_index"], dict_object[key]["load_index"])
    else:
        dict_object[key]["assumed_condition_score"] = max(b_data["condition_score"], dict_object[key]["assumed_condition_score"])
        dict_object[key]["assumed_load_index"] = min(b_data["load_index"], dict_object[key]["assumed_load_index"])

def add_to_map(s_lat, s_long, nearest_start_node, nearest_end_node, si_os_map):
    key = f"{s_lat},{s_long}"
    value = f"{nearest_start_node},{nearest_end_node}"
    si_os_map[key] = [value]

def update_to_map(s_lat, s_long, nearest_start_node, nearest_end_node, si_os_map):
    key = f"{s_lat},{s_long}"
    value = f"{nearest_start_node},{nearest_end_node}"
    si_os_map[key].append(value)