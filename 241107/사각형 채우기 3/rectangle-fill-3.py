N = 1001

dp = [0] * N

dp[0] = 1
dp[1] = 2

for i in range(2, N):
    dp[i] = (dp[i-1] * 2 + dp[i-2] * 3) % 1000000007

n = int(input())
print(dp[n])