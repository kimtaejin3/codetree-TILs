from collections import deque

n, m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

steps = [
    [-1 for _ in range(m)]
    for _ in range(n)
]

def can_go(x, y):
    return in_range(x, y) and steps[x][y] == -1 and grid[x][y] == 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(x, y):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque([(x, y)])
    steps[x][y] = 0

    while q:
        x, y = q.popleft()
        curr_num = steps[x][y]
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                steps[nx][ny] = curr_num + 1
                q.append((nx, ny))

bfs(0, 0)

print(steps[n-1][m-1])