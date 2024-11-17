import sys

INT_MAX = sys.maxsize

N, M = map(int, input().split())

coins = list(map(int, input().split()))
dp = [INT_MAX] * (M + 1) 

dp[0] = 0

for i in range(1, M + 1):
    for j in range(len(coins)):
        if i >= coins[j]:
            dp[i] = min(dp[i], dp[i - coins[j]] + 1)

if dp[M] == INT_MAX:
    print(-1)
else:
    print(dp[M])
