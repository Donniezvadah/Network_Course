"""
Main script for network analysis demonstration.
This script showcases various network analysis techniques using NetworkX.
"""

from visualization.graph_visualizer import visualize_graph, visualize_graph_with_labels
from analysis.graph_operations import create_basic_graph, create_custom_graph
from analysis.matrix_operations import calculate_degrees
from utils.file_operations import load_karate_club_graph

def main():
    # Example 1: Basic graph creation and visualization
    print("Example 1: Basic Graph")
    G = create_basic_graph()
    visualize_graph(G, "basic_graph.png")
    visualize_graph_with_labels(G, "basic_graph_labels.png")
    
    # Example 2: Matrix operations
    print("\nExample 2: Matrix Operations")
    A = G.to_numpy_array()
    degrees = calculate_degrees(A)
    print("Node degrees:", degrees)
    
    # Example 3: Custom graph
    print("\nExample 3: Custom Graph")
    A3 = [[0,1,1,0], [1,0,1,0], [1,1,0,1], [0,0,1,0]]
    G3 = create_custom_graph(A3)
    visualize_graph_with_labels(G3, "custom_graph.png")
    
    # Example 4: Karate Club Graph
    print("\nExample 4: Karate Club Graph")
    K = load_karate_club_graph()
    visualize_graph_with_labels(K, "karate_club.png")
    A_K = K.to_numpy_array()
    degrees = calculate_degrees(A_K)
    print("Karate club node degrees:", degrees)

if __name__ == "__main__":
    main() 