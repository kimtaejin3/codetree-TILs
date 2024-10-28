from collections import deque

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

def can_go(x, y):
    return in_range(x, y) and grid[x][y] != 0 and not visited[x][y] 

def bfs():
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

    q = deque([(0, 0)])
    visited[0][0] = True

    while q:
        curr_v = q.popleft()
        x, y = curr_v[0], curr_v[1]

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if can_go(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))

bfs()

answer = 1 if visited[n-1][m-1] else 0
print(answer)