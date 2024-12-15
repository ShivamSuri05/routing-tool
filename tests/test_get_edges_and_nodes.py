from functions.get_edges_and_nodes import get_data_from_place
import textwrap
# Example usage
place_name = "Hamburg, Germany"  # Correctly spell the place name
result = get_data_from_place(place_name)

# Verify and display results
if result:
    print("Graph data successfully retrieved for Hamburg!")
    print(f"Number of nodes: {len(result['nodes'])}")
    print(f"Number of edges: {len(result['edges'])}")

    # Print a sample of the nodes and edges
    print("\nSample Nodes Data:")
    print(result['nodes'].head().to_string(index=False))  # Display the first few rows of the nodes GeoDataFrame

    print("\nSample Edges Data:")
    edges_string = result['edges'].head().to_string(index=False) # Display the first few rows of the edges GeoDataFrame
    indented_edges = textwrap.indent(edges_string, prefix="    ")
    print(indented_edges)
else:
    print("Failed to retrieve graph data.")