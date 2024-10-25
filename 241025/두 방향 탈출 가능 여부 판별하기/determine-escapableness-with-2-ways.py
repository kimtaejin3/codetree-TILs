n, m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def dfs(x, y):

    dxs, dys = [1, 0], [0, 1]

    for dx, dy in zip(dxs, dys):
        next_x, next_y = x + dx, y + dy
        
        if not in_range(next_x, next_y):
            continue

        if visited[next_x][next_y]:
            continue
        
        if grid[next_x][next_y] == 1:
            visited[next_x][next_y] = True
            dfs(next_x, next_y)

dfs(0, 0)

if visited[n-1][m-1]:
    print(1)
else:
    print(0)