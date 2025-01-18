import osmnx as ox

ox.settings.use_cache = True
#ox.settings.log_console = True
def get_graph_from_place(place_name):
    try:
        custom_filter = '["highway"~"motorway|motorway_link"]' #only considering autobahns
        print("Fetching graph for highway types::",custom_filter)
        graph = ox.graph_from_place(place_name, network_type='drive',custom_filter=custom_filter)
        print(f"Graph fetched for {place_name} successfully")
        return graph
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
