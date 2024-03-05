import heapq

def greedy_best_first_search(graph, start, goal):
    visited = set()
    queue = [(heuristic(start, goal), start)]  # (heuristic, node)

    while queue:
        _, node = heapq.heappop(queue)

        if node == goal:
            return True
        
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(queue, (heuristic(neighbor, goal), neighbor))
    
    return False  # Goal not reachable

# Example graph represented as an adjacency list
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

# Example heuristic function (Euclidean distance)
def heuristic(node, goal):
    coordinates = {'A': (0, 0), 'B': (1, 1), 'C': (2, 2), 'D': (3, 3), 'E': (4, 4), 'F': (5, 5)}
    x1, y1 = coordinates[node]
    x2, y2 = coordinates[goal]
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

start_node = 'A'
goal_node = 'F'

if greedy_best_first_search(graph, start_node, goal_node):
    print("Goal", goal_node, "is reachable from", start_node)
else:
    print("Goal", goal_node, "is not reachable from", start_node)
