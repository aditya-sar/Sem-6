import queue

class Node:
    def __init__(self, name, g_score, f_score):
        self.name = name
        self.g_score = g_score
        self.f_score = f_score

    def __lt__(self, other):
        return self.f_score < other.f_score

class NodeComparer:
    def __call__(self, a, b):
        return a.f_score > b.f_score

def astar(start, goal, graph, heuristic):
    frontier = queue.PriorityQueue()
    frontier.put(Node(start, 0, heuristic[start]))
    g_score = {start: 0}
    f_score = {start: heuristic[start]}
    explored = {}
    while not frontier.empty():
        current = frontier.get()
        if current.name == goal:
            return g_score[current.name]
        if current.name in explored:
            continue
        explored[current.name] = True
        for neigh in range(len(graph[current.name])):
            if graph[current.name][neigh] != 0:
                tentative_g_score = g_score[current.name] + graph[current.name][neigh]
                if neigh in g_score and tentative_g_score >= g_score[neigh]:
                    continue
                g_score[neigh] = tentative_g_score
                f_score[neigh] = tentative_g_score + heuristic[neigh]
                frontier.put(Node(neigh, g_score[neigh], f_score[neigh]))
    return -1

if __name__ == "__main__":
    
    n = int(input("Enter the number of vertices: "))
    m = int(input('Enter number of edges: '))

    graph = [[0 for i in range(n)] for j in range(n)]
    print('Enter edges\nsource destination weight')
    for i in range(m):
        u, v, d = map(int, input().split())
        graph[u][v] = d

    start = int(input("Enter the start node: "))
    goal = int(input("Enter the goal node: "))

    heuristic = [0 for i in range(n)]
    for vertex in range(n):
        heuristic[vertex] = int(input("Enter the heuristic for {}: ".format(vertex)))

    cost = astar(start, goal, graph, heuristic)
    if cost == -1:
        print("Path not found.")
    else:
        print("The minimum cost from {} to {} is {}.".format(start, goal, cost))
