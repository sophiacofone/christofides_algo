def Eulerian_path(): 
    euler_path = []
    removed_edges = []

    for num in ep_with_copies:
        if num not in blacklist:
            euler_path.append(num)
            removed_edges.append(num)
