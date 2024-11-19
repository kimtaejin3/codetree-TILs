N, M = map(int, input().split())
coins = list(map(int, input().split()))
dp = [-1] * (M + 1)
dp[0] = 0

for i in range(1, M + 1):
    for j in range(len(coins)):
        if i - coins[j] >= 0:
            dp[i] = max(dp[i], dp[i - coins[j]] + 1)

print(dp[M])

