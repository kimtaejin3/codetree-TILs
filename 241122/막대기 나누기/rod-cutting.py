n = int(input())
benefits = [0] + list(map(int, input().split()))
dp = [-1] * (n + 1)

dp[0] = 0

for i in range(1, n + 1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i - j] + benefits[j])

print(dp[n])



