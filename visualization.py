#
# Brendan Martin
# visualization.py

import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import drawing_functions as df
import graph_representation as gr



def main(argv):

    num_vertices = int(argv[1])
    graph = gr.gen_graph( num_vertices )
    print(graph)
    
    fig, ax = plt.subplots(2,2, figsize=(8,8))
    
    # OG graph in upper left
    df.draw_graph( graph, ax[0,0] )
    df.draw_title(ax[0,0], "Original Graph")
    plt.draw()
    plt.waitforbuttonpress()
    
    # minimum spanning tree in lower left
    
    df.draw_title(ax[1,0], "T: Minimum Spanning Tree")
    plt.draw()
    plt.waitforbuttonpress()
    
    # odd-degree subgraph in upper right
    
    df.draw_title(ax[0,1], "Odd-degree Subgraph")
    plt.draw()
    plt.waitforbuttonpress()
    
    # perfect matching in upper right
    
    ax[0,1].clear()
    df.draw_title(ax[0,1], "M: Perfect Matching")
    plt.draw()
    plt.waitforbuttonpress()
    
    # Eulerian multigraph in lower right
    
    df.draw_title(ax[1,1], "T U M: Eulerian Multigraph")
    plt.draw()
    plt.waitforbuttonpress()
    
    # Eulerian circuit in lower right
    
    ax[1,1].clear()
    df.draw_title(ax[1,1], "Eulerian Circuit")
    plt.draw()
    plt.waitforbuttonpress()
    
    # Hamiltonian circuit in lower right
    ax[1,1].clear()
    df.draw_title(ax[1,1], "Hamiltonian Circuit")
    plt.draw()
    plt.waitforbuttonpress()


if __name__ == '__main__':
    main(sys.argv)
