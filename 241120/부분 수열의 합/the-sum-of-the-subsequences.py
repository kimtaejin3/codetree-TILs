n, m = tuple(map(int, input().split()))
arr = [0] + list(map(int, input().split()))

dp = [
    [False] * (m + 1)
    for _ in range(n + 1)
]

def initialize():
    dp[0][0] = True

initialize()

for i in range(1, n + 1):
    for j in range(m + 1):
        if j >= arr[i] and dp[i - 1][j - arr[i]]:
            dp[i][j] = True
        
        if dp[i - 1][j]:
            dp[i][j] = True

if dp[n][m]:
    print('Yes')
else:
    print('No')
