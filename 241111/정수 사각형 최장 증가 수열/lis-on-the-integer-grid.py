n = int(input())

num = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [
    [-1 for _ in range(n)]
    for _ in range(n)
]

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def init_dp():
    for i in range(n):
        for j in range(n):
            dp[i][j] = -1

def find_max(x, y):
    if dp[x][y] != -1:
        return dp[x][y]

    best = 1

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        
        if in_range(nx, ny) and num[x][y] < num[nx][ny]:
            best = max(best, find_max(nx, ny) + 1)
            can_go = True
    
    dp[x][y] = best
    return dp[x][y]

ans = -1
for x in range(n):
    for y in range(n):
        ans = max(ans, find_max(x, y))

print(ans)