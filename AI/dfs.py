def dfs(graph, vis, node):
    print(node, end = "")
    vis[node] = True;2

    for adj in graph[node]:
        if vis[adj] == False:
            dfs(graph, vis, adj)


n = int(input("Enter number of nodes: "))
m = int(input("Enter number of edges: "))

graph = [[] for _ in range(n)]

print("Enter nodes in the form of u, v")

for i in range(m):
    u, v = map(int, input().strip().split())
    graph[u].append(v)

vis = [False for i in range(n)]
node = 0

print()

dfs(graph, vis, node)

print()

