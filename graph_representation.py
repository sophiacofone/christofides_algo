#
# Brendan Martin
# graph_representation.py

import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



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
   
