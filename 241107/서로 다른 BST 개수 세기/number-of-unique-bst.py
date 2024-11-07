n = int(input())

if n == 1:
    print(1)
    exit(0)

dp = [0 for _ in range(n + 1)] 

dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = dp[i-1]
    for j in range(1, i):
        dp[i] +=  dp[j] * dp[i - j - 1]
    
print(dp[n])