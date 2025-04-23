"""
Graph visualization module.
Contains functions for visualizing network graphs using NetworkX and Matplotlib.
"""

import matplotlib.pyplot as plt
import networkx as nx

def visualize_graph(graph, output_file="graph.png"):
    """
    Visualize a graph without labels.
    
    Args:
        graph (nx.Graph): NetworkX graph to visualize
        output_file (str): Path to save the visualization
    """
    plt.clf()
    nx.draw(graph)
    plt.savefig(output_file)
    plt.show()

def visualize_graph_with_labels(graph, output_file="graph.png"):
    """
    Visualize a graph with node labels and proper layout.
    
    Args:
        graph (nx.Graph): NetworkX graph to visualize
        output_file (str): Path to save the visualization
    """
    plt.clf()
    pos = nx.spring_layout(graph)
    nx.draw_networkx_labels(graph, pos)
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_edges(graph, pos)
    plt.axis('off')
    plt.savefig(output_file)
    plt.show()

def visualize_graph_with_colors(graph, communities, output_file="graph.png"):
    """
    Visualize a graph with different colors for different communities.
    
    Args:
        graph (nx.Graph): NetworkX graph to visualize
        communities (list): List of node indices for one community
        output_file (str): Path to save the visualization
    """
    plt.clf()
    pos = nx.spring_layout(graph)
    n = len(graph.nodes)
    color = ['r'] * n  # Default color is red
    for node in communities:
        color[node] = 'b'  # Community nodes are blue
    nx.draw_networkx(graph, pos, node_color=color)
    plt.axis('off')
    plt.savefig(output_file)
    plt.show() 