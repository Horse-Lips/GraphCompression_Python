#!/usr/bin/env python

"""
    Gaussian.py: Performs graph compression using the Gaussian elimination method
    Gaussian elimination removes nodes from a graph by creating edges between all
    neighbours of those nodes. When duplicated, the shortest edges will be used.
"""

import copy

__author__ = "Jake Haakanson"
__license__ = "MIT"


def compress(graph: list[list[int]], terminals: list[int]) -> list[list[int]]:
    """
    Compress uses the Gaussian elimination method to compress a graph
    
    Args:
        graph:     A graph given as a weight matrix
        terminals: A set of terminal nodes as a list of ints
    
    Returns:
        graph_compressed: The compressed graph as a weight matrix
    """
    graph_compressed = copy.deepcopy(graph)
    
    for non_terminal in range(len(graph)):
        if non_terminal in terminals: continue  #Ignore terminal nodes
        
        for start_index in range(len(graph_compressed)):
            start_weight = graph_compressed[non_terminal][start_index]  # Weight of edge between start and non_terminal
            if start_weight == 0: continue  # Ignore nodes with no edge
            
            for end_index in range(len(graph_compressed)):
                end_weight = graph_compressed[non_terminal][end_index]  # Weight of edge between end and non_terminal
                if end_weight == 0 or start_index == end_index: continue    # Also skip if start = end
                
                current_weight = graph_compressed[start_index][end_index]   # Weight of old edge
                new_weight = start_weight + end_weight                      # Weight of new edge
                
                if current_weight == 0 or new_weight < current_weight:      # Update edge weight to be shortest > 0
                    graph_compressed[start_index][end_index] = new_weight
                    graph_compressed[end_index][start_index] = new_weight
            
        del graph_compressed[non_terminal]  # Delete non-terminal rows/columns
        for node in graph_compressed:
            del node[non_terminal]
        
    return graph_compressed


g = [#0  1   2   3   4
    [0,  20, 0,  0,  50],   #0
    [20, 0,  15, 10, 0],    #1
    [0,  15, 0,  0,  0],    #2
    [0,  10, 0,  0,  0],    #3
    [50, 0,  0,  0,  0]     #4
]

t = [0, 3, 4]


for node in compress(g, t):
    print(node)
