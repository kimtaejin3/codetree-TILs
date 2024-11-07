MOD = 1000000007
N = 1001

dp = [0] * N

dp[0] = 1
dp[1] = 2

for i in range(2, N):
    dp[i] = (dp[i-1] * 2 + dp[i-2] * 3) % MOD
    for j in range(i-3, -1, -1):
        dp[i] =  (dp[i] + dp[j] * 2) % MOD

n = int(input())
print(dp[n])