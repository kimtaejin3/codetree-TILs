N = 1001

dp = [0] * N

dp[1] = 2
dp[2] = 7

for i in range(3, N):
    dp[i] = (dp[i-1] * 2 + dp[i-2] * 4) % 1000000007

n = int(input())
print(dp[n])