from collections import deque

n, h, m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]
steps = [
    [0 for _ in range(n)]
    for _ in range(n)
]
answer = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(x, y):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    q = deque([(x, y)])
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if in_range(nx, ny) and not visited[nx][ny] and (grid[nx][ny] != 1):
                visited[nx][ny] = True
                steps[nx][ny] = steps[x][y] + 1
                q.append((nx, ny))

def simulate(x, y):
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
            steps[i][j] = 0
    
    bfs(x, y)
    
    temp_results = []

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 3 and steps[i][j] != 0:
                temp_results.append(steps[i][j])
    
    if len(temp_results) == 0:
        answer[x][y] = -1
    else:
        answer[x][y] = min(temp_results)
    
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            simulate(i, j)

for i in range(n):
    for j in range(n):
        print(answer[i][j], end=' ')
    print()