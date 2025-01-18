from functions.get_graph import get_graph_from_place
from functions.save_retrieve_graph import save_graph_sample

def fetch_germany_graph():
    place_name = "Germany"
    graph = get_graph_from_place(place_name)

    graph_filepath = "data/autobahns_germany.graphml"

    result = save_graph_sample(graph, graph_filepath)

    if(result == False):
        print("Some error occurred")
    
    return



if(__name__ == "__main__"):
    print("Starting fetching graph data for the country")
    fetch_germany_graph()
    print("Script ran successfully")