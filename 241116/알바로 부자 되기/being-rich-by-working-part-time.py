N = int(input())

arr = []

for _ in range(N):
    arr.append(tuple(map(int, input().split())))

dp = [0] * N

dp[0] = arr[0][2]

arr.sort()

for i in range(1, N):
    dp[i] = arr[i][2]

    for j in range(i):
        if arr[i][0] > arr[j][1]:
            dp[i] = max(dp[i], dp[j] + arr[i][2])

print(max(dp))
