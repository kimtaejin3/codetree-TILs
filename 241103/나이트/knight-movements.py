from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
r1 = r1 - 1
c1 = c1 - 1
r2 = r2 - 1
c2 = c2 - 1

grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]

steps = [
    [-1 for _ in range(n)]
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(x, y):
    q = deque([(x, y)])
    dxs, dys = [-1, -2, -2, -1, 1, 2, 2, 1], [2, 1, -1, -2, -2, -1, 1, 2]
    steps[x][y] = 0

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if in_range(nx, ny) and steps[nx][ny] == -1:
                steps[nx][ny] = steps[x][y] + 1
                q.append((nx, ny))

bfs(r1, c1)

# for i in range(n):
#     for j in range(n):
#         print(steps[i][j], end=' ')
#     print()

print(steps[r2][c2])