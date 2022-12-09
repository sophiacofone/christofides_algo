def Eulerian_path(): 
    Eulerian_path = []
    removed_edges = []

    for num in ep_with_copies:
        if num not in blacklist:
            final_list.append(num)
            blacklist.append(num)
