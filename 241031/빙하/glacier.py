from collections import deque

n, m = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(x, y):
    q = deque([(x, y)])
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    grid[x][y] = 2

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and grid[nx][ny] == 0:
                grid[nx][ny] = 2
                q.append((nx, ny))

def melt():
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    bfs(0, 0)

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                for dx, dy in zip(dxs, dys):
                    nx, ny = i + dx, j + dy

                    if in_range(nx, ny) and grid[nx][ny] == 2:
                        grid[i][j] = 0
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                grid[i][j] = 0
    
   

ans = 0
t = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            ans += 1

def melt_all():
    global ans, t

    cnt = 0
    t += 1
    melt()

    for row in grid:
        for elem in row:
            if elem == 1:
                cnt += 1
    
    if cnt > 0:
        ans = cnt
    
    if cnt > 0:
        melt_all()

melt_all()

# for row in grid:
#     for elem in row:
#         print(elem, end=' ')
#     print()

# print(t)
# print(ans)
print(t, ans)