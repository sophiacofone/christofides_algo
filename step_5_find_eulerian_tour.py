#Robert Lalani 12.08.22
  '''
  G: (NOT MST OR match)
    [{'1': 1, '2': 18, '3': 16, '4': 11},
    {'0': 1, '2': 8, '3': 6, '4': 15},
    {'0': 18, '1': 8, '3': 4, '4': 14},
    {'0': 16, '1': 6, '2': 4, '4': 14},
    {'0': 11, '1': 15, '2': 14, '3': 14}]

    MatchedMSTree (MST + PerfectMatch)
    [[0, 1, 0], [0, 4, 0], [1, 0, 0], [1, 2, 0], [1, 4, 0], [1, 3, 0], [2, 1, 0], [2, 5, 0], [3, 5, 0], [3, 1, 0], [4, 1, 0], [4, 0, 0], [5, 2, 0], [5, 3, 0]]
  '''

  '''
   
Input Multi_Graph (MST + Perfect Match) in a list of lists

Action: 
'''


    
def find_eulerian_tour(Multigraph):
    # find neigbours
    neighbours = {}
    print('For')
    for edge in Multigraph:
        if edge[0] not in neighbours:
            neighbours[edge[0]] = []

        if edge[1] not in neighbours:
            neighbours[edge[1]] = []
         

        neighbours[edge[0]].append(edge[1])
        neighbours[edge[1]].append(edge[0])

    print("Neighbours: ", neighbours)

    # finds the hamiltonian circuit
    start_vertex = Multigraph[0][0]
    print('start_vertex:', start_vertex)
    eulerian_circut = [neighbours[start_vertex][0]]
    while len(Multigraph) > 0:
        for i, v in enumerate(eulerian_circut):
            if len(neighbours[v]) > 0:
                break

        while len(neighbours[v]) > 0:
            w = neighbours[v][0]

            remove_edge_from_Multigraph(Multigraph, v, w)
            print('Edge Removed:',v,w)
            del neighbours[v][(neighbours[v].index(w))]
            del neighbours[w][(neighbours[w].index(v))]

            i += 1
  
            print(neighbours)
            eulerian_circut.insert(i, w)
        
            

            v = w

    return eulerian_circut


def remove_edge_from_Multigraph(Multigraph, v1, v2):

    for i, item in enumerate(Multigraph):
        if (item[0] == v2 and item[1] == v1) or (item[0] == v1 and item[1] == v2):
            del MatchedMST[i]

    return Multigraph


def main(): 

    G = [{'1': 1, '2': 18, '3': 16, '4': 11},
    {'0': 1, '2': 8, '3': 6, '4': 15},
    {'0': 18, '1': 8, '3': 4, '4': 14},
    {'0': 16, '1': 6, '2': 4, '4': 14},
    {'0': 11, '1': 15, '2': 14, '3': 14}]


    #(MST + PerfectMatch)
    Multigraph = [[0, 1, 0], [0, 4, 0], [1, 0, 0], [1, 2, 0], [1, 4, 0], [1, 3, 0], [2, 1, 0], [2, 5, 0], [3, 5, 0], [3, 1, 0], [4, 1, 0], [4, 0, 0], [5, 2, 0], [5, 3, 0]]

    eulerian_cycle = find_eulerian_tour(Multigraph)

    print(eulerian_cycle) 
