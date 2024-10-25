n, m = map(int, input().split())
graph = [list() for _ in range(n+1)]

vertex_cnt = 0
visited = [False] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())

    graph[x].append(y)
    graph[y].append(x)

def dfs(vertex):
    global vertex_cnt

    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            # print(curr_v)
            vertex_cnt += 1
            visited[curr_v] = True
            dfs(curr_v)

# print(graph)
visited[1] = True
dfs(1)
print(vertex_cnt)