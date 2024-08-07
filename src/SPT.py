#!/usr/bin/env python

"""
    SPT.py: Performs graph compression using the shortest path tree method
    The shortest path tree method created a new graph only including the
    terminal nodes. Edges between these are added using shortest path trees.
"""

import heapq, copy

__author__ = "Jake Haakanson"
__license__ = "MIT"


def compress(graph: list[list[int]], terminals: list[int]) -> list[list[int]]:
    """
    compress uses the shortest path tree method to compress a graph
    
    Args:
        graph:     A graph given as a weight matrix
        terminals: A set of terminal nodes as a list of ints
    
    Returns:
        graph_compressed: The compressed graph as a weight matrix
    """
    graph_compressed = copy.deepcopy(graph)
    
    nodes_kept = list(set(sum([dijkstra(graph, terminal) for terminal in terminals], [])))
    nodes_remove = []
    
    for non_terminal in range(len(graph)):  # Reconstruct graph only keeping required nodes
        if non_terminal in terminals or non_terminal in nodes_kept: continue
        nodes_remove.append(non_terminal)
        
        for node in graph_compressed:
            node[non_terminal] = 0
    
    for non_terminal in nodes_kept:
        if non_terminal in terminals or sum([neighbour > 0 for neighbour in graph_compressed[non_terminal]]) != 2: continue
        nodes_remove.append(non_terminal)
        
        indices = [i for i, v in enumerate(graph_compressed[non_terminal]) if v > 0]
        weight = graph_compressed[non_terminal][indices[0]] + graph_compressed[non_terminal][indices[1]]
        
        graph_compressed[indices[0]][indices[1]] = weight
        graph_compressed[indices[1]][indices[0]] = weight
    
    nodes_remove.sort(reverse = True)
    
    for to_remove in nodes_remove:
        del graph_compressed[to_remove]  # Delete non-terminal rows/columns
        for node in graph_compressed:
            del node[to_remove]
        
    return graph_compressed


def dijkstra(graph: list[list[int]], start_node: int) -> list[int]:
    """
    dijkstra uses Dijkstra's algorithm to calculate shortest path
    trees from starting nodes. Returns only terminals to keep.
    
    Args:
        graph:      A graph given as a weight matrix
        terminals:  A set of terminal nodes as a list of ints
        start_node: Start node of shortest path tree
    
    Returns:
        nodes_kept: List of terminals to remain in the graph
    """
    dists = [float("inf")] * len(graph)
    dists[start_node] = 0               # Add start as dist 0
    prioq = [(0, start_node)]
    nodes_kept = set()
    
    while prioq:
        current_dist, current_node = heapq.heappop(prioq)
        if current_dist > dists[current_node]: continue # Skip if dist is greater than lowest found
        
        for neighbour_node, neighbour_weight in enumerate(graph[current_node]):
            if neighbour_weight == 0: continue                  # Ignore non-existent edges
            neighbour_dist = current_dist + neighbour_weight    # Calculate new dist

            if neighbour_dist < dists[neighbour_node]:  # Update dist if lower than lowest
                dists[neighbour_node] = neighbour_dist
                nodes_kept.add(current_node)     # Update previous node
                heapq.heappush(prioq, (neighbour_dist, neighbour_node))

    return list(nodes_kept)
