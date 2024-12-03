#dp[i][j]: i번까지 시행했을때 j번개의 빨간카드가 있을때 합의 최댓값
#dp[i][j] = max(dp[i-1][j-1] + 빨간카드, dp[i-1][j] + 파란카드)

N = int(input())
arr = [(0, 0)]

for i in range(2 * N):
    r, b = map(int, input().split())
    arr.append((r, b))

dp = [
    [0] * (N + 1)
    for _ in range(2 * N + 1)
]

dp[0][0] = 0

dp[1][0] = arr[1][1]
dp[1][1] = arr[1][0]

for i in range(2, 2 * N + 1):
    for j in range(N + 1):
        if j < 1:
             dp[i][j] = max(dp[i][j], dp[i - 1][j] + arr[i][1])
             continue

        dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + arr[i][0], dp[i - 1][j] + arr[i][1])

# for i in range(2 * N + 1):
#     for j in range(N + 1):
#         print(dp[i][j], end=' ')
#     print()

print(dp[2 * N][N])
