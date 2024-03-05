from sys import maxsize
from itertools import permutations

def calculate_total_distance(order, distances):
    total_distance = 0
    for i in range(len(order) - 1):
        total_distance += distances[order[i]][order[i+1]]
    total_distance += distances[order[-1]][order[0]]  # Return to the starting city
    return total_distance

def traveling_salesman_bruteforce(distances):
    num_cities = len(distances)
    all_possible_orders = permutations(range(num_cities))

    min_distance = float('inf')
    best_order = None

    for order in all_possible_orders:
        total_distance = calculate_total_distance(order, distances)
        if total_distance < min_distance:
            min_distance = total_distance
            best_order = order

    return best_order, min_distance

# Example usage:
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

best_order, min_distance = traveling_salesman_bruteforce(distances)
print(f"Best order: {best_order}")
print(f"Minimum distance: {min_distance}")
