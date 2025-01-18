from functions.limited_data import get_excel_data
from functions.save_retrieve_graph import use_saved_graph_sample
from functions.add_bund_in_edge import add_bund_in_edge
from functions.save_json import save_json_to_file

def create_bund_edge_database():
    filepath = "data/bridge_data.xlsx"
    columns_to_fetch = ['condition_score', 'load_index', 'type', 'latitude', 'longitude']
    b_data = get_excel_data(filepath, columns_to_fetch)

    graph_filepath = "data/autobahns_germany.graphml"
    graph = use_saved_graph_sample(graph_filepath)
    bund_obj = {}
    start_idx = 10000  # Example start index
    end_idx = 16000
    bd_os_map = {}
    print(f"File will be saved to:: data/edges_and_bridges_{start_idx}-{end_idx}.json")
    for row in b_data.iloc[start_idx:end_idx].itertuples():
        print(f"Processing row:",row.Index)
        add_bund_in_edge(
            graph, 
            row.latitude, 
            row.longitude, 
            row.condition_score,
            row.load_index,
            row.type,
            bund_obj,
            bd_os_map
        )
    
    bridge_data_filepath = f"data/edges_and_bridges_{start_idx}-{end_idx}.json"
    save_json_to_file(bund_obj, bridge_data_filepath)
    mapping_data_filepath = f"data/bund_osmnx_map_{start_idx}-{end_idx}.json"
    save_json_to_file(bd_os_map, mapping_data_filepath)


if(__name__ == "__main__"):
    print("Creating bund edge data for the dataset")
    create_bund_edge_database()
    print("Script ran successfully")