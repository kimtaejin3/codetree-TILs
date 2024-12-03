INF = 10 ** 9

n, k = map(int, input().split())

a = [0] + list(map(int, input().split()))

dp = [[-INF for _ in range(k + 1)] for _ in range(n + 1)]
ans = -INF

for i in range(1, n + 1):
    if a[i] >= 0:
        for j in range(k + 1):
            dp[i][j] = max(dp[i - 1][j] + a[i], a[i])
            ans = max(ans, dp[i][j])
    else:
        for j in range(1, k + 1):
            dp[i][j] = max(dp[i - 1][j - 1] + a[i], a[i])
            ans = max(ans, dp[i][j])

print(ans)

