MAX_N = 1000

dp = [0] * (MAX_N + 1)

dp[2] = 1
dp[3] = 1

for i in range(4, MAX_N + 1):
    dp[i] = (dp[i - 2] + dp[i - 3]) % 10007

n = int(input())
print(dp[n])