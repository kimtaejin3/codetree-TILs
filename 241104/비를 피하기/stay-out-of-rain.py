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

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(shelters):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    for x, y in shelters:
        visited[x][y] = True

    q = deque(shelters[:])

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if in_range(nx, ny) and not visited[nx][ny] and (grid[nx][ny] != 1):
                visited[nx][ny] = True
                steps[nx][ny] = steps[x][y] + 1
                q.append((nx, ny))

def simulate():
    shelters = []

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 3:
                shelters.append((i, j))
    
    bfs(shelters)

simulate()

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            if steps[i][j] == 0:
                print(-1, end=' ')
            else:
                print(steps[i][j], end=' ')

        else:
            print(0, end=' ')

    print()