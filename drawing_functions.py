#
# Brendan Martin
# drawing_functions.py

import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Calculate the (x,y) position of "vertex"
def vertex_coordinates(vertex, num_vertices):
    radius = 9
    
    # calc angle, jitter slightly
    angle = vertex * (2*np.pi)/num_vertices
    angle += (2*np.random.rand(1)-1) * (2*np.pi)/(8*num_vertices)
    
    x = radius * np.cos(angle)
    y = radius * np.sin(angle)
    
    return x, y

# Draw the vertex to the image
def draw_vertex(vertex, vert_coors, num_vertices, image):
    x, y = vert_coors[0], vert_coors[1]
    
    circ = plt.Circle( (x,y), 1, color='b', zorder=num_vertices*num_vertices )
    image.add_patch( circ )
    image.text( x, y, str(vertex), zorder=num_vertices*num_vertices, ha='center' )
    
    return

# Draw the edge from edge_start to edge_end, also the weight of the edge
def draw_edge(v1_coors, v2_coors, num_vertices, weight, image):
    x1, y1 = v1_coors[0], v1_coors[1]
    x2, y2 = v2_coors[0], v2_coors[1]
    
    # Interpolate to find a place to draw the edge weight
    lamb = np.random.rand(1)
    xt = lamb*x1 + (1-lamb)*x2
    yt = lamb*y1 + (1-lamb)*y2
    
    image.plot([x1,x2],[y1,y2], 'y')
    image.text( xt, yt, weight )
    
    return
   
# Draw a representation of the given graph to the given image
def draw_graph( graph, image ):
    num_vertices = len(graph)
    
    # Get coordinates of all vertices, draw vertices
    vert_coors = np.zeros((num_vertices, 2))
    for vert in range(num_vertices):
        vert_coors[vert] = vertex_coordinates(vert, num_vertices)
        draw_vertex(vert, vert_coors[vert], num_vertices, image)
    
    # draw all edges
    for v1 in range(len(graph)):
        for v2 in graph[v1].keys():
            v2 = int(v2)
            if v2 > v1:
                weight = graph[v1][str(v2)]
                draw_edge(vert_coors[v1], vert_coors[v2], num_vertices, weight, image)
    
    return

# Draw a title to the given image
def draw_title(ax, title):
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 12)
    
    ax.set_xticks([])
    ax.set_yticks([])
    
    ax.text( 0, 11, title, size='large', ha='center' )
    return
    

