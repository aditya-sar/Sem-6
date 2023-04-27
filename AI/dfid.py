def dfs(graph, vis, node, count, depth):
    if count > depth:
        return
    print(node, end = " ")
    vis[node] = True

    for newNode in graph[node]:
        if vis[newNode] == False:
            dfs(graph, vis, newNode, count+1, depth)


n = int(input("Enter number of nodes: "))
m = int(input("Enter number of edges: "))

graph = [[] for i in range(n)]
print("Enter edges U to V")
for i in range(m):
    u, v = map(int, input().strip().split())
    graph[u].append(v)

depth = int(input("Enter max depth: "))

for i in range(depth):
    node = 0
    vis = [False for i in range(n)]
    count = 0
    print("Iteration ", i+1)
    dfs(graph, vis, node, count, i)
    print()
