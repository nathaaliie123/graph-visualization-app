import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# Title of the application
st.title("Interactive Graph Visualization App")

# Input: Number of nodes and edges
st.subheader("Graph Parameters")
num_nodes = st.number_input("Enter the number of nodes:", min_value=1, step=1)
num_edges = st.number_input("Enter the number of edges:", min_value=0, step=1)

# Input: Edge connections
st.subheader("Define the edges")
edges = []
for i in range(int(num_edges)):
    edge = st.text_input(f"Enter edge {i + 1} (e.g., 1 2):")
    if edge:
        try:
            node1, node2 = map(int, edge.split())
            edges.append((node1, node2))
        except ValueError:
            st.error("Invalid edge format. Use the format: node1 node2.")

# Button to generate the graph
if st.button("Generate Graph"):
    # Create a graph
    graph = nx.Graph()
    graph.add_nodes_from(range(1, int(num_nodes) + 1))
    graph.add_edges_from(edges)

    # Visualize the graph
    st.subheader("Graph Visualization")
    plt.figure(figsize=(8, 6))
    nx.draw(graph, with_labels=True, node_color="skyblue", node_size=500, font_size=10, edge_color="gray")
    st.pyplot(plt)
