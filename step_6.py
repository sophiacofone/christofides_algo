from step_5_find_eulerian_tour import find_eulerian_tour

def convert_Eulerian_Circuit(eulerian_Circut): 
    approx_optimial_path = []
    removed_edges = []

    for vertex in eulerian_Circut:
        if vertex not in removed_edges:
            approx_optimial_path.append(vertex)
            removed_edges.append(vertex)
    return approx_optimial_path

def main(): 
    eulerian_circut = [1, 0, 4, 1, 0, 4, 1, 2, 1, 3, 5, 2, 5, 3, 1]
    
    hamiltonian_Circut = convert_Eulerian_Circuit(eulerian_circut)
    print(hamiltonian_Circut)
    
