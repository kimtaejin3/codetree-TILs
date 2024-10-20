import sys
sys.setrecursionlimit(10**4)

n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

grid_d = [
    list(map(int, input().split()))
    for _ in range(n)
]

r, c = map(int, input().split())
r, c = r - 1, c - 1

dxs, dys = [-1, -1, 0, 1, 1, 1, 0, -1],[0, 1, 1, 1, 0, -1, -1, -1]

ans = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move(x, y, depth):
    global ans
    nx, ny = x + dxs[grid_d[x][y] - 1], y + dys[grid_d[x][y] - 1]

    while in_range(nx,ny):
        if grid[x][y] < grid[nx][ny]:
            move(nx, ny, depth + 1)
        
        nx, ny = nx + dxs[grid_d[x][y] - 1], ny + dys[grid_d[x][y] - 1]

    ans = max(ans, depth)

move(r, c, 0)
print(ans)