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
    graph = [{'1': 1, '2': 12, '3': 13},
            {'0': 1, '2': 17, '3': 13},
            {'0': 12, '1': 17, '3': 3},
            {'0': 13, '1': 13, '2': 3}]
    
    X = kruskal(graph)

    src_dict, brendan_version = convert_vis(graph,X)

    odd_nodes, graph_odd, brendan_graph_odd = find_odd(src_dict)
    print(graph_odd)
    print(brendan_graph_odd)
    print(odd_nodes)
    

if __name__ == '__main__':
    main()

