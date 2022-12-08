#Guyriano Charles
#CS5800
#Fall 2022

#This function finds the minimum weight matching and adds it to MST generating a multi-graph.
def minimumWeightedMatching(MST, G, odd_vert):
    '''Input: The minimum weight spanning tree, the original graph as a list of dictionaries, the list of odd vertices
        Output: A multigraph
    '''
    
	while odd_vert:
		v = odd_vert.pop()
		dist = -1
		u = 1
		nearest = 0
		for u in odd_vert:
			if G[v][u] > dist :
				dist = G[v][u]
				nearest = u
		
		MST.insert(v, dict({nearest: dist}))
		odd_vert.remove(nearest)
		
	return MST


