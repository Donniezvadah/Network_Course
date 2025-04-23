"""
File operations module.
Contains functions for loading and saving graph data.
"""

import networkx as nx

def load_karate_club_graph(file_path='karate.txt'):
    """
    Load the Karate Club graph from a file.
    
    Args:
        file_path (str): Path to the graph data file
        
    Returns:
        nx.Graph: NetworkX graph object
    """
    return nx.read_weighted_edgelist(file_path)

def save_graph(graph, file_path):
    """
    Save a graph to a file.
    
    Args:
        graph (nx.Graph): NetworkX graph to save
        file_path (str): Path to save the graph
    """
    nx.write_edgelist(graph, file_path) 