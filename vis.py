#
# Brendan Martin
# vis.py

import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



def gen_graph( num_vertices ):
    graph = []
    
    for v in range(num_vertices):
        dict = {  }
        for v2 in range(num_vertices):
            if v != v2:
                weight = np.random.randint(1,21)
                dict[str(v2)] = weight
        graph.append(dict)
    
    return graph
    
    

# For a video, calc optical flow at each time step, estimate the next frame based on current pixel velocities
def main(argv):

    num_vertices = int(argv[1])
    print(num_vertices)
    graph = gen_graph( num_vertices )
    print(graph)


if __name__ == '__main__':
    main(sys.argv)
