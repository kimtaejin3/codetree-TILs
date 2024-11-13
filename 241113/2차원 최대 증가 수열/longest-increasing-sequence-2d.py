n, m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [
    [-1 for _ in range(m)]
    for _ in range(n)
]

dp[0][0] = 0

for i in range(1, n):
    for j in range(1, m):
        for k in range(i):
            for l in range(j):
                if dp[k][l] == -1:
                    continue
                
                if grid[i][j] <= grid[k][l]:
                    continue
                
                dp[i][j] = max(dp[i][j], dp[k][l] + 1)

ans = -1
for i in range(n):
    for j in range(m):
        ans = max(ans, dp[i][j])

print(ans + 1)



