from collections import deque
import sys

n, k = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

steps = [
    [sys.maxsize for _ in range(n)]
    for _ in range(n)
]

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r1, c1 = r1-1, c1-1
r2, c2 = r2-1, c2-1

walls = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]
selected_walls = []
len_walls = len(walls)

def initialize_steps():
    for i in range(n):
        for j in range(n):
            steps[i][j] = sys.maxsize

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs():
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque([(r1, c1)])
    steps[r1][c1] = 0

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if in_range(nx, ny) and steps[nx][ny] == sys.maxsize and grid[nx][ny] == 0:
                steps[nx][ny] = steps[x][y] + 1
                q.append((nx, ny))

def simulate():
    ans = -1

    initialize_steps()

    for wall in selected_walls:
        x, y = wall
        grid[x][y] = 0

    bfs()    

    ans = steps[r2][c2]

    for wall in selected_walls:
        x, y = wall
        grid[x][y] = 1
    
    return ans

ans = sys.maxsize
def select_walls(lev, cnt):
    global ans
    
    if cnt == k:
        ans = min(ans, simulate())
        return

    if lev == len_walls:
        return
    
    selected_walls.append(walls[lev])
    select_walls(lev + 1, cnt + 1)
    selected_walls.pop()

    select_walls(lev + 1, cnt)

select_walls(0, 0)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)