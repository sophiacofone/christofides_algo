# Python3 program to print Eulerian circuit in given
# directed graph using Hierholzer algorithm
def printCircuit(adj):
 
    # adj represents the adjacency list of
    # the directed graph
    # edge_count represents the number of edges
    # emerging from a vertex
    edge_count = dict()
    
    print("EC:", edge_count)
    print("Starting first for loop for EC")
    for i in range(len(adj)):
        
        # find the count of edges to keep track
        # of unused edges
        edge_count[i] = len(adj[i])
        print("EC:", edge_count)
 
    if len(adj) == 0:
        return # empty graph
 
    # Maintain a stack to keep vertices
    curr_path = []
 
    # vector to store final circuit
    circuit = []
 
    # start from any vertex
    curr_path.append(0)
    curr_v = 0 # Current vertex
 
    while len(curr_path):
        print("\n\n\n")
        print("CP:", curr_path)
        print("Circ:", circuit)
        print("Curr_V:", curr_v)
        print("EC:", edge_count)
 
        # If there's remaining edge
        print("===========")
        
        if edge_count[curr_v]:
            print("Edge count at node", curr_v, "> 0!")
            # Push the vertex
            print("Adding curr_v to path")
            print("CP Before:", curr_path)
            curr_path.append(curr_v)
            print("CP After :", curr_path)
 
            # Find the next vertex using an edge
            next_v = adj[curr_v][-1]
            print("Making next vertex", next_v)
 
            # and remove that edge
            print("Removing edge from EC")
            print("EC Before:", edge_count)
            edge_count[curr_v] -= 1
            print("EC After :", edge_count)
            print("Removing edge from adj matrix")
            print("adj before:", adj)
            adj[curr_v].pop()
            print("adj after :", adj)
            
 
            # Move to next vertex
            curr_v = next_v
            print("Updating curr_v to", curr_v)
 
        # back-track to find remaining circuit
        else:
            print("Edge count at node", curr_v, "== 0 (ELSE STATEMENT)")
            
            print("Adding curr_v to circuit")
            
            print("Circ before:", circuit)
            circuit.append(curr_v)
            print("Circ after :", circuit)
            # Back-tracking
            
            print("Back tracking to previous node")
            curr_v = curr_path[-1]
            print("New curr_v =", curr_v)
            
            print("Removing last item from curr_path")
            print("CP Before:", curr_path)
            curr_path.pop()
            print("CP After :", curr_path)
 
    # we've got the circuit, now print it in reverse
    for i in range(len(circuit) - 1, -1, -1):
        print(circuit[i], end = "")
        if i:
            print(" -> ", end = "")
 
# Driver Code
if __name__ == "__main__":
 
    # Input Graph 1
    adj1 = [0] * 3
    for i in range(3):
        adj1[i] = []
 
    # Build the edges
    adj1[0].append(1)
    adj1[1].append(2)
    adj1[2].append(0)
    printCircuit(adj1)
    print()
 
    # Input Graph 2
    adj2 = [0] * 7
    for i in range(7):
        adj2[i] = []
 
    adj2[0].append(1)
    adj2[0].append(6)
    adj2[1].append(2)
    adj2[2].append(0)
    adj2[2].append(3)
    adj2[3].append(4)
    adj2[4].append(2)
    adj2[4].append(5)
    adj2[5].append(0)
    adj2[6].append(4)
    #printCircuit(adj2)
    print()
 
# This code is contributed by
# sanjeev2552