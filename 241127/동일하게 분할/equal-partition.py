n = int(input())
arr = [0] + list(map(int, input().split()))

m = sum(arr)

dp = [
    [False] * (m + 1)
    for _ in range(n + 1)
]

dp[0][0] = True

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if j - arr[i] >= 0 and dp[i - 1][j - arr[i]]:
            dp[i][j] = True
        
        if dp[i - 1][j]:
            dp[i][j] = True

for i in range(1, m + 1):
    if dp[n][i] and i == (m - i):
        print('Yes')
        break

else:
    print('No')

        

