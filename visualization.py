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
import Final_Project_Steps_3_4 as s34
import step_5_find_eulerian_tour as s5
import step_6 as s6


def main(argv):
    # Generate a random graph with the given number of vertices
    num_vertices = int(argv[1])
    graph = gr.gen_graph( num_vertices )
    print(graph)
    
    # Generate the coordinates of each vertex of the graph for visualization purposes
    vert_coors = df.get_vertex_coors(num_vertices)
    
    # Init display window with four plots
    fig, ax = plt.subplots(2,2, figsize=(8,8))
    
    # Draw the original graph in upper left corner
    df.draw_graph( graph, ax[0,0], vert_coors, num_vertices )
    df.draw_title(ax[0,0], "Original Graph")
    plt.draw()
    plt.waitforbuttonpress()
    
    # draw minimum spanning tree in lower left
    MST = s1.kruskal(graph) #generate minimum spanning tree
    src_dict, MST = s1.convert_vis(graph, MST, num_vertices)
    df.draw_graph( MST, ax[1,0], vert_coors, num_vertices )
    df.draw_title(ax[1,0], "T: Minimum Spanning Tree")
    plt.draw()
    plt.waitforbuttonpress()
    
    # odd-degree subgraph in upper right
    odd_verts, _, _ = s2.find_odd(src_dict)
    df.draw_odd_verts( odd_verts, ax[0,1], vert_coors, num_vertices )
    df.draw_title(ax[0,1], "Odd-degree Subgraph")
    plt.draw()
    plt.waitforbuttonpress()
    
    ax[0,1].clear() # clear odd-degree vertex drawing to make way for perfect matching
    
    # perfect matching in upper right
    MST, matching = s34.minimumWeightedMatching(MST, graph, odd_verts)
    
    print("matching")
    print(matching)
    
    matching_std = gr.convert_vis_dict(matching, num_vertices) # convert matching to standard graph format for display
    df.draw_graph( matching_std, ax[0,1], vert_coors, num_vertices )
    df.draw_title(ax[0,1], "M: Perfect Matching")
    plt.draw()
    plt.waitforbuttonpress()
    
    # Eulerian multigraph in lower right
    multigraph = s34.formMultigraph(MST, matching)
    df.draw_graph( multigraph, ax[1,1], vert_coors, num_vertices )
    df.draw_title(ax[1,1], "T U M: Eulerian Multigraph")
    plt.draw()
    plt.waitforbuttonpress()
    
    
    # Rearrange some graphs
    
    ax[0,1].clear() # clear perfect matching
    ax[1,0].clear() # clear MST
    ax[1,1].clear() # clear eulerian multigraph
    
    df.draw_graph( multigraph, ax[1,0], vert_coors, num_vertices )
    df.draw_title(ax[1,0], "T U M: Eulerian Multigraph")
    
    
    # Eulerian circuit in lower right
    print("multi 1:")
    print(multigraph)
    
    multigraph = gr.convert_vis_dict_to_list(multigraph, num_vertices) # convert multigraph format
    
    print("multi 2:")
    print(multigraph)
    
    eulerian_circuit = s5.find_eulerian_tour(multigraph, graph, ax[1,1], vert_coors, num_vertices)
    
    print("euler")
    print(eulerian_circuit)
    
    df.draw_euler_circuit( eulerian_circuit, graph, ax[1,1], vert_coors, num_vertices )
#    df.draw_graph( eulerian_cycle_std, ax[1,1], vert_coors, num_vertices )
    df.draw_title(ax[1,1], "Eulerian Circuit")
    plt.draw()
    plt.waitforbuttonpress()
    
    
    # move eulerian circuit up one plot
    ax[1,1].clear()
    df.draw_euler_circuit( eulerian_circuit, graph, ax[0,1], vert_coors, num_vertices )
    df.draw_title(ax[0,1], "Eulerian Circuit")
    
    
    # Hamiltonian circuit in lower right
    hamiltonian_cycle = s6.convert_Eulerian_Circuit(eulerian_circuit, graph, ax[1,1], vert_coors, num_vertices)
    df.draw_ham_cycle( hamiltonian_cycle, graph, ax[1,1], vert_coors, num_vertices )
#    df.draw_graph( hamiltonian_circuit, ax[1,1], vert_coors, num_vertices )
    df.draw_title(ax[1,1], "Hamiltonian Circuit")
    plt.draw()
    plt.waitforbuttonpress()


if __name__ == '__main__':
    main(sys.argv)
