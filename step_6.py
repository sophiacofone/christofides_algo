def Eulerian_path(): 
    euler_path = []
    removed_edges = []

    for num in euler_path:
        if num not in removed_edges:
            euler_path.append(num)
            removed_edges.append(num)
