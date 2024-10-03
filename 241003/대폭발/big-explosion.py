n, m, r, c = tuple(map(int,input().split()))
grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]

next_grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def expand(x, y, dist):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx * dist, y + dy * dist
        if in_range(nx, ny):
            next_grid[nx][ny] = 1

def simulate(dist):
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0
    
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                expand(i, j, dist)
    
    for i in range(n):
        for j in range(n):
            if next_grid[i][j]:
                grid[i][j] = 1

grid[r-1][c-1] = 1

dist = 1

for _ in range(m):
    simulate(dist)
    dist *= 2

ans = sum([
    grid[i][j]
    for i in range(n)
    for j in range(n)
])

print(ans)