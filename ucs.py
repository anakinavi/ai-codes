import heapq

def uniform_cost_search(graph, start, goal):
    visited = set()
    queue = [(0, start, [])]  # (cost, node, path)

    while queue:
        cost, node, path = heapq.heappop(queue)
        
        if node == goal:
            return path + [node]
        
        if node not in visited:
            visited.add(node)
            for neighbor, edge_cost in graph[node].items():
                heapq.heappush(queue, (cost + edge_cost, neighbor, path + [node]))
    
    return None  # Goal not reachable

# Example graph represented as an adjacency list
graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'C': 1, 'D': 5},
    'C': {'D': 8},
    'D': {'E': 2},
    'E': {}
}

start_node = 'A'
goal_node = 'E'

result = uniform_cost_search(graph, start_node, goal_node)
if result:
    print("Path from", start_node, "to", goal_node, ":", result)
else:
    print("Goal", goal_node, "not reachable from", start_node)
