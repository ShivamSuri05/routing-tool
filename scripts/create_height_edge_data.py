from functions.limited_data import get_excel_data
from functions.save_retrieve_graph import use_saved_graph_sample
from functions.add_height_in_edge import add_height_in_edge
from functions.save_json import save_json_to_file

def create_height_edge_database():
    filepath = "data/siemens_height.xlsx"
    columns_to_fetch = ['Lat_CORR', 'Long_CORR', 'Hauteur_Droite_cm']
    s_data = get_excel_data(filepath, columns_to_fetch)

    graph_filepath = "data/germany.graphml"
    graph = use_saved_graph_sample(graph_filepath)
    height_obj = {}
    si_os_map = {}
    for row in s_data.itertuples():
        print(f"Processing row:",row.Index)
        add_height_in_edge(graph, row.Lat_CORR, row.Long_CORR, row.Hauteur_Droite_cm, height_obj, si_os_map)

    height_data_filepath = "data/edges_and_height.json"
    save_json_to_file(height_obj, height_data_filepath)
    mapping_data_filepath = "data/siemens_osmnx_map.json"
    save_json_to_file(si_os_map, mapping_data_filepath)


if(__name__ == "__main__"):
    print("Creating height edge data for the dataset")
    create_height_edge_database()
    print("Script ran successfully")