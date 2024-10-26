N, M = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(N)
]

temp_ans = 0

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def can_go(x, y):
    global visited

    return in_range(x, y) and not visited[x][y] and grid[x][y] > k

def dfs(x, y, k):
    global visited

    dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if can_go(nx, ny):
            visited[nx][ny] = True
            dfs(nx, ny, k)


ans_safe_area_cnt = -1
ans_k = -1

for k in range(1, 101):
    
    safe_area_cnt = 0
    
    visited = [
        [False for _ in range(M)]
        for _ in range(N)
    ]

    for n in range(N):
        for m in range(M):
            if grid[n][m] > k and not visited[n][m]:
                safe_area_cnt += 1
                visited[n][m] = True
                dfs(n, m, k)
    
    if ans_safe_area_cnt < safe_area_cnt:
        ans_safe_area_cnt = safe_area_cnt
        ans_k = k

print(ans_k, ans_safe_area_cnt)