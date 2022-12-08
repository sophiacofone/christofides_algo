# Sophia Cofone, 11/27/22
'''
This file is for step 1 of algorithm (finding the MST of a given graph)
Using Kruskal's algorithm for MST
Includes a pre-defined graph for testing
I wanted to the source node explicit for testing purposes, so the sort_by_weight function transforms the graph representation
The convert_vis brings the representation back to the way Brendan had set it up (and provides a dictonary of dictonaries for more clarity)
'''

def makeset(graph):
    '''
    Input: Brendan's gen_graph output
    Action:
        for all of the indices in the graph list,
        create a list of list with each index being the "singleton" element
    Output: gives us the initial list of lists with each vertex in its own list
    '''
    return [[i] for i in range(len(graph))]

def sort_by_weight(graph):
    '''
    Input: Brendan's gen_graph output
    Action:
        Reworking the representation to include both the source and destination nodes, as well as weight.
        Then sorting by weight.
    Output:
        is a 'table' aka list of lists with source being first, dest being second, and weight being last
    '''

    table = []
    for i,src in enumerate(graph):
        for j,dest in enumerate(src):
            table.append([i,int(dest),src[dest]])
    table.sort(key=lambda x: x[2])
    
    return table

def find(vertex,tracker_list):
    '''
    Input: the vertex we want to know what set it is in, and the node tracker list
    Action:
        for all of the sub-sets in the node_tracker list,
        count the times the target vertex appears in the sub set list, if > 0 then true
    Output: gives us the index of the set the target is in
    '''

    return [s.count(vertex)>0 for s in tracker_list].index(True)

def union_tracker_list(tracker_list,i,j):
    '''
    Input:
        current tracker_list of nodes (starts as a list of lists with each node in its own list, but progressivly becomes one sub-list/set as nodes get moved in)
        i and j are the indices of the 2 "sub-sets"
    Action:
        Step 1: merge together 2 "sub-sets", becomes mini-list
        Step 2: given each value ("sub-set") in the node_tracker list,
        if the index is not one of the sub sets we just merged (the rest of the "untouched" elements),
        then that set is included in the new list
        Step 3: merge together the new mini-list and the old "untouched" sub-sets
    Output: Updated node_tracker list
    Note that this is what causes the algo to "stop", because eventually all nodes will be in one sub-set
    '''

    return [tracker_list[i]+tracker_list[j]] + [value for index,value in enumerate(tracker_list) if index not in [i,j]]

def kruskal(graph):
    '''
    Input: Brendan's gen_graph output
    Action:
        create initial list of lists that are the source nodes
        create sorted version of graph by weight
        for all of the elements in the sorted graph
            find the set that first value belongs to
            find the set that second value belongs to
            if they are in different sets
                add that edge to the MST list (X)
                merge the two values together
            if they are in the same set
                skip
    Output: MST in list of list form
    '''
    X=[]
    node_tracker = makeset(graph)
    sorted_graph = sort_by_weight(graph)
    for i in range(len(sorted_graph)):
        subset1 = find(sorted_graph[i][0],node_tracker)
        subset2 = find(sorted_graph[i][1],node_tracker)
        if subset1 != subset2:
            edge_weight = [sorted_graph[i][0],sorted_graph[i][1],sorted_graph[i][2]]
            X.append(edge_weight)
            node_tracker = union_tracker_list(node_tracker,subset1,subset2)
    
    return X

def convert_vis(graph,X,num_vertices):
    '''
    Input:
        Brendan's gen_graph output
        Kruskal function output (list of lists)
    Action: converts the list of list representation back to the list of dictionaries representation
    Output: MST in dictionary representation
    Note that this also includes a dictionary of dictionaries (src_dict) for clarity
    '''
    src_dict = {src:{} for src in range(num_vertices)}
    
    #create empty dictionary for each node
    
    for i,_set in enumerate(X):
        # from src to dest
        src_dict[_set[0]][str(_set[1])] = _set[2]
        # from dest to src
        src_dict[_set[1]][str(_set[0])] = _set[2]

    brendan_version = list(src_dict.values())

    return src_dict, brendan_version

def main():

    #for testing
    num_vertices = 4
    graph = [{'1': 1, '2': 12, '3': 13},
            {'0': 1, '2': 17, '3': 13},
            {'0': 12, '1': 17, '3': 3},
            {'0': 13, '1': 13, '2': 3}]
    
    X = kruskal(graph)
    print(X)

    src_dict, brendan_version = convert_vis(graph,X,num_vertices)
    print(src_dict)
    print(brendan_version)


if __name__ == '__main__':
    main()
