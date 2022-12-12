#Robert Lalani 12.08.22
from Final_Project_Steps_3_4 import minimumWeightedMatching

import drawing_functions as df
import matplotlib.pyplot as plt

'''
   
Input Multi_Graph (MST + Perfect Match) in a list of lists
Action:
  for all edges in the Multigraph
  Create a dictionary for vertices and their neighbours  {Key is vertex: [ list of neighbours ]
  
  v1 : [ v2, v3, ...]
  v2
  v3
  ...
  
  Cycles through graph, records path until all edges have been visted.
  
  Output: Eulerian Circut as a list
 
'''


    
def find_eulerian_tour(Multigraph, graph, image, vert_coors, num_vertices):
    
    #Dictionary: Keys are the vertices in the Multigraph
    #Value is a list of neighbors
    neighbours = {}
    for edge in Multigraph:
        if edge[0] not in neighbours: #Add to dictionary neighbours v[u] :[ v[w] ]
            neighbours[edge[0]] = []

        if edge[1] not in neighbours: #Add to dictionary neighbours v[w] :[ v[u] ]
            neighbours[edge[1]] = []
         

        neighbours[edge[0]].append(edge[1])

    print("Neighbours: ", neighbours)

    # finds the hamiltonian circuit
     # Start at the first vertex (can be arbitrary)
    start_vertex = Multigraph[0][0]
    print('start_vertex:', start_vertex)
    
    #Keeps track of the Eulerian Tour
    eulerian_circuit = [neighbours[start_vertex][0]]
    while len(Multigraph) > 0:
        #enumerates path
        for i, v in enumerate(eulerian_circuit):
            if len(neighbours[v]) > 0:
                break
        #While vertex has neighbors
        while len(neighbours[v]) > 0:
            # Key : Selected Vertex ,
            # Value: First Element in Neighbor list
            w = neighbours[v][0]
             
            # Remove the first value in {vertices : [ list of neighbors] }
            # Delete edge from the Multigraph : [ list of neighbors] }
            remove_edge_from_Multigraph(Multigraph, v, w)
            print('Edge Removed:',v,w)
            del neighbours[v][(neighbours[v].index(w))]
            del neighbours[w][(neighbours[w].index(v))]

            i += 1
  
            print(neighbours)
            print(Multigraph)
            eulerian_circuit.insert(i, w)  # Add vertex to tour path

            v = w # Move selected vertex to w
            
            # Draw current eulerian_circuit to
            image.clear()
            df.draw_euler_circuit( eulerian_circuit, graph, image, vert_coors, num_vertices )
            df.draw_title(image, "")
            plt.draw()
            plt.waitforbuttonpress()

    return eulerian_circuit


def remove_edge_from_Multigraph(Multigraph, v1, v2):
    # Flags indicating whether the first instance of an edge has been encountered
    found_to = False
    found_from = False
    
    # For all edges in the graph
    i = 0
    while i < len(Multigraph):
        #Remove the first instance of the edge from v1 to v2
        if ((not found_to) and Multigraph[i][0] == v1 and Multigraph[i][1] == v2):
            found_to = True
            del Multigraph[i]
            i = i-1 #Adjust edge index since an edge was deleted
        
        #Remove the second instance of the edge from v2 to v1
        if ((not found_from) and Multigraph[i][0] == v2 and Multigraph[i][1] == v1):
            found_from = True
            del Multigraph[i]
            i = i-1 #Adjust edge index since an edge was deleted
            
        i = i+1
        

    return Multigraph

'''
def main():

    G = [{'1': 1, '2': 18, '3': 16, '4': 11},
    {'0': 1, '2': 8, '3': 6, '4': 15},
    {'0': 18, '1': 8, '3': 4, '4': 14},
    {'0': 16, '1': 6, '2': 4, '4': 14},
    {'0': 11, '1': 15, '2': 14, '3': 14}]


    #(MST + PerfectMatch)
    Multigraph = [[0, 1, 0], [0, 4, 0], [1, 0, 0], [1, 2, 0], [1, 4, 0], [1, 3, 0], [2, 1, 0], [2, 5, 0], [3, 5, 0], [3, 1, 0], [4, 1, 0], [4, 0, 0], [5, 2, 0], [5, 3, 0]]

    eulerian_cycle = find_eulerian_tour(Multigraph)

    print("cycle")
    print(eulerian_cycle)

if __name__ == '__main__':
    main()
'''    
