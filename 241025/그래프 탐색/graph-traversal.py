n, m = map(int, input().split())
graph = [list() for _ in range(n+1)]

visited = [False] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())

    graph[x].append(y)

def dfs(curr_vertex):
    for vertex in graph[curr_vertex]:
        if not visited[vertex]:
            # print(vertex)
            visited[vertex] = True
            dfs(vertex)

# print(graph)
dfs(1)
print(sum([1 for elem in visited if elem == True]))