INT_MAX = 1000001
n = int(input())

num = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [
    [INT_MAX for _ in range(n)]
    for _ in range(n)
]

dp[0][0] = num[0][0]
for i in range(1, n):
    dp[0][i] = min(dp[0][i - 1], num[0][i])

for i in range(1, n):
    dp[i][0] = min(dp[i - 1][0], num[i][0])

for i in range(1, n):
    for j in range(1, n):
        if num[i][j] <= dp[i-1][j] and num[i][j] <= dp[i][j-1]:
            dp[i][j] = num[i][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# for row in dp:
#     for elem in row:
#         print(elem, end=' ')
#     print()

print(dp[n-1][n-1])