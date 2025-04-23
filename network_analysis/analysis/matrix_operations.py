"""
Matrix operations module.
Contains functions for performing matrix operations on graph adjacency matrices.
"""

import numpy as np

def calculate_degrees(adjacency_matrix):
    """
    Calculate the degree of each node from the adjacency matrix.
    
    Args:
        adjacency_matrix (np.array): Adjacency matrix of the graph
        
    Returns:
        np.array: Array of node degrees
    """
    n = len(adjacency_matrix)
    e = np.ones(n)
    return np.dot(adjacency_matrix, e)

def matrix_power(adjacency_matrix, power):
    """
    Calculate the power of an adjacency matrix.
    
    Args:
        adjacency_matrix (np.array): Adjacency matrix of the graph
        power (int): Power to raise the matrix to
        
    Returns:
        np.array: Resulting matrix
    """
    result = adjacency_matrix.copy()
    for _ in range(power - 1):
        result = np.dot(result, adjacency_matrix)
    return result 