n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))
dp = [
    [-1, 0]
    for _ in range(n + 1)
]

dp[0][0] = 0
dp[1][0] = arr[1]

if arr[1] < 0:
    dp[1][1] = 1

for i in range(2, n + 1):
    if arr[i] < 0:
        dp[i][1] += dp[i - 1][1] + 1
    else:
        dp[i][1] = dp[i - 1][1]
    
    if dp[i][1] > k:
        if arr[i] >= 0:
            dp[i][0] = arr[i]
        continue
    
    dp[i][0] = max(arr[i], dp[i - 1][0] + arr[i])

max_val = -1     
for i in range(n + 1):
    max_val = max(dp[i][0], max_val)
    
print(max_val)
