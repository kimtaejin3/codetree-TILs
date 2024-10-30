from collections import deque

n, k, m = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

start_positions = []

for _ in range(k):
    r, c = map(int, input().split())
    start_positions.append((r-1, c-1))

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

def init_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

stone_positions = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            stone_positions.append((i, j))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs():
    q = deque(start_positions)
    
    dxs, dys = [1, -1, 0, 0], [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        visited[x][y] = True

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if in_range(nx, ny) and grid[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

choose = []
c_selected = []
def select_m(lev, cnt):
    global selected

    if cnt == m:
        c_selected.append(choose[:])
        return
    
    if lev == len(stone_positions):
        return
    
    choose.append(stone_positions[lev])
    select_m(lev + 1, cnt + 1)

    choose.pop()
    select_m(lev + 1, cnt)

ans = -1
def move():
    global c_selected, ans
    c_selected = []
    select_m(0, 0)

    for s in c_selected:

        for ss in s:
            x, y = ss
            grid[x][y] = 0

        init_visited()
        
        bfs()

        cnt = 0
        for i in range(n):
            for j in range(n):
                if visited[i][j]:
                    cnt += 1
        ans = max(ans, cnt)
        for ss in s:
            x, y = ss
            grid[x][y] = 1
    

move()
print(ans)