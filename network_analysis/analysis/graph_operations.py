"""
Graph operations module.
Contains functions for creating and manipulating network graphs.
"""

import networkx as nx
import numpy as np

def create_basic_graph():
    """
    Create a basic graph with predefined edges.
    
    Returns:
        nx.Graph: A NetworkX graph object
    """
    G = nx.Graph()
    edges = [(1,6), (1,2), (1,3), (1,5), (2,3), (3,4), (4,5), (5,6), (6,2)]
    G.add_edges_from(edges)
    return G

def create_custom_graph(adjacency_matrix):
    """
    Create a graph from an adjacency matrix.
    
    Args:
        adjacency_matrix (list or np.array): Adjacency matrix representation of the graph
        
    Returns:
        nx.Graph: A NetworkX graph object
    """
    return nx.from_numpy_array(np.array(adjacency_matrix))

def remove_edges(graph, edges_to_remove):
    """
    Remove specified edges from a graph.
    
    Args:
        graph (nx.Graph): Original graph
        edges_to_remove (list): List of edges to remove
        
    Returns:
        nx.Graph: Modified graph with edges removed
    """
    H = graph.copy()
    H.remove_edges_from(edges_to_remove)
    return H 