def bfs(graph, vis, node, q):    
    while q:
        sz = len(q)
        for i in range(sz):
            node = q.pop(0)
            if vis[node] == True:
                continue
            print(node, end = " ")
            for adj in graph[node]:
                q.append(adj)
        print()

n = int(input("Enter number of nodes: "))
m = int(input("Enter number of edges: "))

graph = [[] for i in range(n)]

print("Enter nodes in form of u, v")

for count in range(m):
    u, v = map(int, input().strip().split())
    graph[u].append(v)

q = []
q.append(0)
vis = [False for i in range(n)]
node = 0

print()
bfs(graph, vis, node, q)
print()
