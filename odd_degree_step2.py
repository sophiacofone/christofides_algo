# Sophia Cofone, 11/28/22
'''
This file is for step 2 of algorithm (finding the set of vertices with odd degree)
Includes a pre-defined graph for testing
'''

from mst_step1 import kruskal, convert_vis

def find_odd(src_dict):
    '''
    Input: MST in dictonary of dictonaries format
    Action: 
        for all of the nodes in the graph (whole dict),
            if the length of node1(value) is odd
                add node0(key) and node1(value) to the new dict
    Output: gives us the updated dictonary of dictonaries with only odd degree,
    updated list of dictonaries with only odd degree,
    and just a list of verticies with odd degree
    '''
    src_dict_odd = {}
    for node in src_dict.items():
        if len(node[1]) %2 != 0:
            src_dict_odd[node[0]] = node[1]
            
    odd_nodes = list(src_dict_odd.keys())
    graph_odd = src_dict_odd
    brendan_graph_odd = list(src_dict_odd.values())
    
    return odd_nodes, graph_odd, brendan_graph_odd 

def main():

    #for testing
    num_vertices = 6
    graph = [{'1': 5, '2': 18, '3': 18, '4': 8, '5': 8}, 
{'0': 5, '2': 1, '3': 12, '4': 2, '5': 11}, 
{'0': 18, '1': 1, '3': 18, '4': 15, '5': 6}, 
{'0': 18, '1': 12, '2': 18, '4': 19, '5': 8}, 
{'0': 8, '1': 2, '2': 15, '3': 19, '5': 9}, 
{'0': 8, '1': 11, '2': 6, '3': 8, '4': 9}]
    
    X = kruskal(graph)

    src_dict, brendan_version = convert_vis(graph,X,num_vertices)

    odd_nodes, graph_odd, brendan_graph_odd = find_odd(src_dict)
    print(graph_odd)
    print(brendan_graph_odd)
    print(odd_nodes)

if __name__ == '__main__':
    main()

