n = int(input())

arr = list(map(int, input().split()))

dp = [[0, 0] for _ in range(n)]

dp[0][0] = 1
dp[0][1] = 1

for i in range(1, n):
    max_val = 0
    max_val2 = 0

    for j in range(i):
        if arr[j] < arr[i]:
            max_val = max(max_val, dp[j][0])
        elif arr[j] > arr[i]:
            max_val2 = max(max_val2, dp[j][1], dp[j][0])

    dp[i][0] = max_val + 1
    dp[i][1] = max_val2 + 1

max_val = -1

for i in range(n):
    a, b = dp[i]
    max_val = max(max_val, a, b)

print(max_val)
