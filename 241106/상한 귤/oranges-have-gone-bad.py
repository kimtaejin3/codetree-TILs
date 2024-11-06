from collections import deque

n, k = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]
steps = [
    [-1 for _ in range(n)]
    for _ in range(n)
]
positions = [
    (i,j)
    for i in range(n)
    for j in range(n)
    if grid[i][j] == 2
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs():
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    q = deque(positions)

    for position in positions:
        x, y = position
        steps[x][y] = 0
        visited[x][y] = True
    
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == 1:
                steps[nx][ny] = steps[x][y] + 1
                visited[nx][ny] = True
                q.append((nx, ny))

bfs()

for i in range(n):
    for j in range(n):
        if steps[i][j] == -1 and grid[i][j] == 1:
            steps[i][j] = -2

for i in range(n):
    for j in range(n):
        print(steps[i][j], end=' ')
    print()