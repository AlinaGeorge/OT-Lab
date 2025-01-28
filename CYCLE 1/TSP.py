import itertools

def calculate_total_distance(distance_matrix, path):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distance_matrix[path[i]][path[i + 1]]
    total_distance += distance_matrix[path[-1]][path[0]] 
    return total_distance


def tsp_bruteforce(distance_matrix):
    n = len(distance_matrix)
    cities = list(range(n))
    

    all_permutations = itertools.permutations(cities)
    
    min_distance = float('inf')
    best_path = None
    
    for path in all_permutations:
        current_distance = calculate_total_distance(distance_matrix, path)
        if current_distance < min_distance:
            min_distance = current_distance
            best_path = path
    
    return best_path, min_distance

distance_matrix = [
    [0, 2, 2, 5, 9, 3],
    [2, 0, 4, 6, 7, 8],
    [2, 4, 0, 8, 6, 3],
    [5, 6, 8, 0, 4, 9],
    [9, 7, 6, 4, 0, 10],
    [3, 8, 3, 9, 10, 0]
]

best_path, min_distance = tsp_bruteforce(distance_matrix)

print("Best Path:", best_path)
print("Minimum Distance:", min_distance)
