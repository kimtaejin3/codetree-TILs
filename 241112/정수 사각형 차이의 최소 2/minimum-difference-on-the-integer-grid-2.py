import sys

INT_MAX = sys.maxsize
MAX_R = 100

n = int(input())
num = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [
    [
        [INT_MAX] * (MAX_R + 1)
        for _ in range(n)
    ]
    for _ in range(n)
]

def initialize():
    for i in range(n):
        for j in range(n):
            for k in range(1, MAX_R + 1):
                dp[i][j][k] = INT_MAX
    
    dp[0][0][num[0][0]] = num[0][0]

    for i in range(1, n):
        for k in range(1, MAX_R + 1):
            dp[i][0][min(k, num[i][0])] = min(
                dp[i][0][min(k, num[i][0])],
                max(dp[i - 1][0][k], num[i][0])
            )
    
    for j in range(1, n):
        for k in range(1, MAX_R + 1):
            dp[0][j][min(k, num[0][j])] = min(
                dp[0][j][min(k, num[0][j])],
                max(dp[0][j - 1][k], num[0][j])
            )

def solve():
    initialize()

    for i in range(1, n):
        for j in range(1, n):
            for k in range(1, MAX_R + 1):
                dp[i][j][min(k, num[i][j])] = min(
                    dp[i][j][min(k, num[i][j])],
                    max(min(dp[i - 1][j][k], dp[i][j - 1][k]), num[i][j])
                )

solve()

ans = INT_MAX

for k in range(1, MAX_R + 1):
    if dp[n-1][n-1][k] != INT_MAX:
        ans = min(ans, dp[n-1][n-1][k] - k)

print(ans)
