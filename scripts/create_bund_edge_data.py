from functions.limited_data import get_excel_data
from functions.save_retrieve_graph import use_saved_graph_sample
from functions.add_bund_in_edge import add_bund_in_edge
from functions.save_json import save_json_to_file

def create_bund_edge_database():
    filepath = "data/bridge_data.xlsx"
    columns_to_fetch = ['condition_score', 'load_index', 'type', 'latitude', 'longitude']
    b_data = get_excel_data(filepath, columns_to_fetch)

    graph_filepath = "data/germany.graphml"
    graph = use_saved_graph_sample(graph_filepath)
    bund_obj = {}
    #si_os_map = {}
    for row in b_data.itertuples():
        print(f"Processing row:",row.Index)
        add_bund_in_edge(
            graph, 
            row.latitude, 
            row.longitude, 
            row.condition_score,
            row.load_index,
            row.type,
            bund_obj
        )
    
    bridge_data_filepath = "data/edges_and_bridges.json"
    save_json_to_file(bund_obj, bridge_data_filepath)


if(__name__ == "__main__"):
    print("Creating bund edge data for the dataset")
    create_bund_edge_database()
    print("Script ran successfully")