from functions.route_prediction import get_all_routes
from functions.utils import convert_to_float
from functions.save_retrieve_graph import use_saved_graph_sample
from functions.get_edges_and_nodes import get_nearest_edge_data

def fetch_paths(src, dst, height, buffer_height, num_paths):
    src = src.split(" ")
    start_point = (convert_to_float(src[0]), convert_to_float(src[1]))
    dst = dst.split(" ")
    end_point = (convert_to_float(dst[0]), convert_to_float(dst[1]))
    buffer_height = convert_to_float(buffer_height)
    height = convert_to_float(height)
    num_paths = int(num_paths)
    print(start_point, end_point, height, buffer_height)
    valid_filepath = "data/autobahns_germany_with_restrictions.graphml"
    loaded_graph = use_saved_graph_sample(valid_filepath)
    try:
        paths = get_all_routes(loaded_graph, start_point, end_point, num_paths , buffer_height+height)
        #paths = [[93014209, 1594531855, 491164, 491179, 491180, 491213, 94170412, 491220, 5789574746, 510617, 94170191, 94170196, 491788, 94074641, 326893039, 94074560, 1384522839, 1659223892, 95966208, 11981282, 95966399, 253043428, 253043456, 253043400, 21573263, 30845029, 280763543, 249245581, 21424998, 21424650, 268273247, 2887358771, 21424636], [93014209, 1594531855, 491164, 491179, 491180, 491213, 94170412, 491220, 5789574746, 510617, 94170191, 94170196, 491788, 94074641, 326893039, 94074560, 1384522839, 1659223892, 95966208, 11981282, 11981293, 95966399, 253043428, 253043456, 253043400, 21573263, 30845029, 280763543, 249245581, 21424998, 21424650, 268273247, 2887358771, 21424636], [93014209, 1594531855, 491164, 491179, 491180, 491213, 94170412, 491220, 5789574746, 510617, 94170191, 94170196, 491788, 94074641, 326893039, 94074560, 1384522839, 1659223892, 95966208, 11981282, 95966399, 253043428, 253043438, 253043456, 253043400, 21573263, 30845029, 280763543, 249245581, 21424998, 21424650, 268273247, 2887358771, 21424636], [93014209, 1594531855, 491164, 491179, 491180, 491213, 94170412, 491220, 5789574746, 510617, 94170191, 94170196, 491788, 94074641, 326893039, 94074560, 1384522839, 1659223892, 95966208, 11981282, 95966399, 253043428, 253043456, 253043400, 21573261, 21573263, 30845029, 280763543, 249245581, 21424998, 21424650, 268273247, 2887358771, 21424636], [93014209, 1594531855, 491164, 491179, 491180, 491213, 94170412, 491220, 5789574746, 510617, 94170191, 94170196, 491788, 94074641, 326893039, 94074560, 1384522839, 1659223892, 95966208, 11981282, 95966399, 253043428, 253043456, 253043400, 21573263, 30845029, 280763543, 249245581, 21424998, 21424650, 268273247, 110057419, 2887358771, 21424636]]
        print(paths)
        formatted_response = []
        for path in paths:
            path_list = []

            for i in range(len(path) - 1):
                node1 = path[i]
                node2 = path[i + 1]

                edge_data = get_nearest_edge_data(loaded_graph, node1, node2)
                coord1 = (loaded_graph.nodes[node1]['y'], loaded_graph.nodes[node1]['x'])
                path_list.append([node1, coord1])  # Always append the starting node
                
                if 'geometry' in edge_data:
                    geometry_coordinates = str(edge_data[0].geometry)
                    print("geometry_coordinates:", geometry_coordinates)

                    # Extract coordinates from LINESTRING format
                    coordinates_str = geometry_coordinates.replace("LINESTRING (", "").replace(")", "")
                    coordinate_pairs = coordinates_str.split(", ")
                    coordinates_list = [tuple(map(float, coord.split())) for coord in coordinate_pairs]

                    # Convert to (latitude, longitude) and append each point
                    for coor in coordinates_list:
                        path_list.append((coor[1], coor[0]))  # Swap to (lat, lon)

                else:
                    print(f"No geometry data for edge {node1} -> {node2}")

            # Append the last node in the path
            last_node = path[-1]
            coord_last = (loaded_graph.nodes[last_node]['y'], loaded_graph.nodes[last_node]['x'])
            path_list.append([last_node, coord_last])  # Append the last node
            
            formatted_response.append(path_list)

        return formatted_response

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
        return "No Paths Found"