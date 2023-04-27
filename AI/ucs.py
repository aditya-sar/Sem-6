import heapq

def ucs(graph, start, goal):
    visited = set()
    heap = [(0, start, [])]
    while heap:
        (cost, node, path) = heapq.heappop(heap)
        if node not in visited:
            visited.add(node)
            path.append(node)
            if node == goal:
                return (cost, path)
            for neighbor, neighbor_cost in graph[node].items():
                if neighbor not in visited:
                    heapq.heappush(heap, (cost + neighbor_cost, neighbor, path))
    return float('inf')

graph = {
    'a' : {'b':7, 'c':3},
    'b' : {'a':7, 'c':2, 'e':7},
    'c' : {'a':3, 'b':2, 'd':9},
    'd' : {'c':9, 'e':3, 'h':13},
    'e' : {'d':3, 'f':2, 'g':1},
    'f' : {'e':2},
    'g' : {'e':1},
    'h' : {'d':1},
}

start = 'a'
goal = 'g'

cost, path = ucs(graph, start, goal)

print(f"The shortest path from {start} to {goal} is {path} with cost {cost}")
