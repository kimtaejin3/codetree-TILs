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

    can_go = False
    for dx, dy in zip(dxs, dys):
        prev_x, prev_y = x + dx, y + dy
        
        if in_range(prev_x, prev_y) and num[x][y] > num[prev_x][prev_y]:
            dp[x][y] = max(dp[x][y], find_max(prev_x, prev_y) + 1)
            can_go = True
    
    if not can_go:
        return 1
    else:
        return dp[x][y]

ans = -1
for x in range(n):
    for y in range(n):
        ans = max(ans, find_max(x,y))

print(ans)