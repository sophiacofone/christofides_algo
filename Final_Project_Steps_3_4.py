#Guyriano Charles
#CS5800
#Fall 2022

#This function finds the minimum weight matching 
def minimumWeightedMatching(MST, G, odd_vert):
    '''Input: The minimum weight spanning tree, the original graph as a list of dictionaries, the list of odd vertices
       Output: A multigraph, the MST
    '''
    oddvert_ToJoin = {}

    while odd_vert:
        v = odd_vert.pop(0) #pop off the first odd degree vertex in the list
        print("\nfor " + str(v) + "\n")
        weight = float('inf') #set the weight to inf initially
        nearest = 0 #set the nearest node to 0 initially, this is arbitrary
        for u in odd_vert: #for all other nodes in odd_vert besides v
                    u = str(u)
                    if G[v][u] < weight : #if a weight lower than the one previously established is found, set the weight of (v, u) in G to that weight
                            weight = G[v][u]
                            print("weight " + str(weight) + "\n")
                            nearest = u
                            print("nearest " + str(nearest) + "\n")

        oddvert_ToJoin[v] = [nearest, weight]
        odd_vert.remove(int(nearest))

    return MST, oddvert_ToJoin

#This function adds the minimum weight matching to the MST generating a multi-graph.
def formMultigraph(MST, ToJoin):
    '''Input: an MST, a dictionary containing the edges to add and their weights
       Output: A multigraph
    '''

    for v in ToJoin.keys():     

        MST.insert(v, dict({ToJoin[v][0]: ToJoin[v][1]})) #add the edges from the matching to the MST
    
    return MST

def main():
    
    G = [{'1': 5, '2': 18, '3': 18, '4': 8, '5': 8}, 
{'0': 5, '2': 1, '3': 12, '4': 2, '5': 11}, 
{'0': 18, '1': 1, '3': 18, '4': 15, '5': 6}, 
{'0': 18, '1': 12, '2': 18, '4': 19, '5': 8}, 
{'0': 8, '1': 2, '2': 15, '3': 19, '5': 9}, 
{'0': 8, '1': 11, '2': 6, '3': 8, '4': 9}]

    MinST = [{'1': 5}, {'2': 1, '4': 2, '0': 5}, {'1': 1, '5': 6}, {'5': 8}, {'1': 2}, {'2': 6, '3': 8}]

    odd_vert = [0, 1, 3, 4]
    
    MST, ToJoin = minimumWeightedMatching(MinST, G, odd_vert)

    multGraph = formMultigraph(MST, ToJoin)

    print(multGraph)

main()


