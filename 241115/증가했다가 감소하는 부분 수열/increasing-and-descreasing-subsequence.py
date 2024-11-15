n = int(input())
num = list(input().split())

dp = [
    [1 for _ in range(2)]
    for _ in range(n)
]

for i in range(1, n):
    for j in range(i):
        if num[i] > num[j]:
            dp[i][0] = max(dp[i][0], dp[j][0] + 1)
        elif num[i] < num[j]:
            dp[i][1] = max(dp[i][1], dp[j][1] + 1, dp[j][0] + 1)

ans = -1
for i in range(n):
    ans = max(ans, dp[i][0], dp[i][1])

print(ans)
