### Robert Lalani
### 12.01.22
### CS5800 - Final Project Step 5 example code

import random
import time


'''
Example graph:

v0		v1
	
	v2

v3		v4

Tour starts at vertex 0 (it can be random vertex)
An example of a tour would be: 

v0 -> v1 -> v2 ->  v3 -> v4 -> v2 -> v0 

Code below code WILL NOT do this... it will repeat a cycle 

Example output: 

[0, 1, 2, 0, 1, 2, 4, 3, 2]

Need to fix how to select next node from available paths, right now its random. 

'''



# Input (x,y) if list[0] = x return other vertex
# else return x
def find_other_num(num, list):
    print("Find Next Element", num, list)
    if list[0] == num:
        return list[1]
    else:
        return list[0]

# Using below as an example of a Multigraph to input for step 5
# 4 nodes - 1,2,3,4
# [0,1] represents and edge between vertex 0,1
Multigraph_paths = [[0, 1], [0, 2], [1, 2], [2, 3], [2,4], [3,4]]


path_of_nodes = []
visted_edges = set()
previous_path = None




# Starting with the frist node[0][0] for testing purposes 
# To do: switch current_node to take in a random vertex 
current_node = Multigraph_paths[0][0] # 0



while len(visted_edges) < len(Multigraph_paths):
    time.sleep(1)
    print("Current node:", current_node)
    path_of_nodes.append(current_node)

    # Get the paths for the current node
    available_paths = []


    for path in Multigraph_paths:
        if current_node in path:
            available_paths.append(path)
	
	# If vertex does not have a previous path, ignore
    try:
        available_paths.remove(previous_path)
    except: pass

    print("Available paths:", available_paths)

    # Randomly choose an available path
    next_path = random.choice(available_paths)
    print("Next path", next_path)

	# Finds which vertex is being selected
    current_node = find_other_num(current_node, next_path)
    previous_path = next_path

    visted_edges.add( str(next_path) )
    print(len(visted_edges))
    print("Current node (end of loop):", current_node)

else:
    path_of_nodes.append(current_node)




# Includes copies, will fix
print(path_of_nodes)

        






