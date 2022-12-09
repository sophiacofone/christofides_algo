def convert_Eulerian_Circuit(eulerian_circut): 
    approx_optimial_path = []
    removed_edges = []

    for num in euler_path:
        if num not in removed_edges:
            euler_path.append(num)
            removed_edges.append(num)
    return approx_optimial_path
   
