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

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and grid[x][y] == 0

def bfs(x, y):
    dxs, dys = [1,-1,0,0],[0,0,-1,1]
    q = deque([(x, y)])
    visited[x][y] = True

    while q:
        curr_v = q.popleft()
        x, y = curr_v[0], curr_v[1]

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))


for _ in range(k):
    x, y = map(int, input().split())
    bfs(x-1, y-1)

ans = 0
for i in range(n):
    for j in range(n):
        ans += visited[i][j]

print(ans)