def find_eulerian_tour(Multi_Graph, G):

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

  """
   
Input Multi_Graph (MST + Perfect Match) in a list of lists

Action:   For every edge in the multigraph:

                If node 0 shares an edge node 1
                  Add node 0 key and node 1 value neighbour dict
                If node 1 shares an edge node 1 0
                  Add node 0 key and node 1 value neighbour dict
    neighbours_dict_Output: Neighbours Dictionary - Key is vertex, Value is  vertices who share an edge

    """
def find_eulerian_tour(MatchedMSTree, G):
    # find neigbours
    neighbours = {}
    print('For')
    for edge in MatchedMSTree:
        if edge[0] not in neighbours:
            neighbours[edge[0]] = []

        if edge[1] not in neighbours:
            neighbours[edge[1]] = []
         

        neighbours[edge[0]].append(edge[1])
        neighbours[edge[1]].append(edge[0])

    print("Neighbours: ", neighbours)

    # finds the hamiltonian circuit
    start_vertex = MatchedMSTree[0][0]
    print('start_vertex:', start_vertex)
    eulerian_tour = [neighbours[start_vertex][0]]
    while len(MatchedMSTree) > 0:
        for i, v in enumerate(eulerian_tour):
            if len(neighbours[v]) > 0:
                break

        while len(neighbours[v]) > 0:
            w = neighbours[v][0]

            remove_edge_from_matchedMST(MatchedMSTree, v, w)
            print('Edge Removed:',v,w)
            del neighbours[v][(neighbours[v].index(w))]
            del neighbours[w][(neighbours[w].index(v))]

            i += 1
  
            print(neighbours)
            eulerian_tour.insert(i, w)
        
            

            v = w

    return eulerian_tour


def remove_edge_from_matchedMST(MatchedMST, v1, v2):

    for i, item in enumerate(MatchedMST):
        if (item[0] == v2 and item[1] == v1) or (item[0] == v1 and item[1] == v2):
            del MatchedMST[i]

    return MatchedMST
