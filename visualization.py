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
import mst_step1 as s1
import odd_degree_step2 as s2



def main(argv):

    num_vertices = int(argv[1])
    graph = gr.gen_graph( num_vertices )
    vert_coors = df.get_vertex_coors(num_vertices)
    print(graph)
    
    fig, ax = plt.subplots(2,2, figsize=(8,8))
    
    # OG graph in upper left
    df.draw_graph( graph, ax[0,0], vert_coors, num_vertices )
    df.draw_title(ax[0,0], "Original Graph")
    plt.draw()
    plt.waitforbuttonpress()
    
    # minimum spanning tree in lower left
    
    mst = s1.kruskal(graph) #generate minimum spanning tree
    src_dict, mst = s1.convert_vis(graph, mst, num_vertices) #convert mst to graph representation expected by drawing function
    df.draw_graph( mst, ax[1,0], vert_coors, num_vertices )
    df.draw_title(ax[1,0], "T: Minimum Spanning Tree")
    plt.draw()
    plt.waitforbuttonpress()
    
    # odd-degree subgraph in upper right
    odd_verts, _, _ = s2.find_odd(src_dict)
    df.draw_odd_verts( odd_verts, ax[0,1], vert_coors, num_vertices )
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
