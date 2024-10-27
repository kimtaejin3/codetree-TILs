n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]
block_cnt = 0
max_block_cnt_per_one = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(x, y):
    global block_cnt_per_one
    dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        
        if in_range(nx, ny) and not visited[nx][ny] and grid[x][y] == grid[nx][ny]:
            visited[nx][ny] = True
            block_cnt_per_one += 1
            dfs(nx, ny)

for x in range(n):
    for y in range(n):
        if not visited[x][y]:
            block_cnt_per_one = 1
            visited[x][y] = True
            dfs(0, 0)

            if block_cnt_per_one >= 4:
                block_cnt += 1
        
            max_block_cnt_per_one = max(block_cnt_per_one, max_block_cnt_per_one)

print(block_cnt, max_block_cnt_per_one)