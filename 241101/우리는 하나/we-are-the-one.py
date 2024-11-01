from collections import deque

n, k, u, d = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

coordinates = []

for i in range(n):
    for j in range(n):
        coordinates.append((i,j))

choose = []

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    return in_range(x, y) and not visited[x][y]

def bfs(arr):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque(arr)

    while q:
        x, y = q.popleft()
        visited[x][y] = True

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny) and u <= abs(grid[nx][ny] - grid[x][y]) <= d:
                visited[nx][ny] = True
                q.append((nx, ny))

    return

ans = -1
def pick(idx, lev):
    global ans
    
    if lev == k:
        # print(choose)
        for i in range(n):
            for j in range(n):
                visited[i][j] = False

        bfs(choose[:])

        cnt = 0
        for i in range(n):
            for j in range(n):
                if visited[i][j]:
                    cnt += 1
        ans = max(ans, cnt)
        return
    
    for i in range(idx, len(coordinates)):
        choose.append(coordinates[i])
        pick(i + 1, lev + 1)
        choose.pop()

pick(0, 0)
print(ans)