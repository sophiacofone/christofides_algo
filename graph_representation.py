#
# Brendan Martin
# graph_representation.py

import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Generate a graph of the given size with random edge weights
def gen_graph( num_vertices ):
    graph = []
    
    # For all pairs of vertices
    for v in range(num_vertices):
        dict = {  }
        for v2 in range(num_vertices):
            # Don't assign an edge leading to itself
            if v != v2:
                # Ensure we don't assign two different weights to one bidirectional edge
                if v2 < v:
                    weight = graph[v2][str(v)]
                else:
                    weight = np.random.randint(1,21)
                # Create new edge
                dict[str(v2)] = weight
        # Add completed adjacency list to graph structure
        graph.append(dict)
    
    return graph



# Convert step 3,4 output to standard graph representation
def convert_vis_dict(X, num_vertices):
    src_dict = {src:{} for src in range(num_vertices)}
    for source,dest in X.items():
        # from src to dest
        src_dict[source][dest[0]] = dest[1]
        # from dest to src
        src_dict[int(dest[0])][str(source)] = dest[1]

    brendan_version = list(src_dict.values())

    return brendan_version


# Convert step 4 output to step 5 input format
def convert_vis_dict_to_list(X, num_vertices):
    ls = []

    for source, dict in enumerate(X):
        for dest,weight in dict.items():
            # from src to dest
            ls.append( [source, int(dest), weight] )
            # from dest to src
#            ls.append( [int(dest), source, weight] )

    return ls

# Convert step 5 output to standard format
def convert_euler_cycle(X, num_vertices):
    src_dict = {src:{} for src in range(num_vertices)}
    for i in range(0, len(X) - 2, 2):
        edge = X[i:i+3]
        # from src to dest
        print(edge[0])
        print(edge[2])
        src_dict[edge[0]][str(edge[2])] = edge[1]
        # from dest to src
        src_dict[edge[2]][str(edge[0])] = edge[1]
        
    edge = X[i:i+3]
    src_dict[X[0]][str(X[-2])] = X[-1]
    src_dict[X[-2]][str(X[0])] = X[-1]

    brendan_version = list(src_dict.values())

    return brendan_version
