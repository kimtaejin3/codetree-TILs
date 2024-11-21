N, M = map(int, input().split())

ws = [0]
vs = [0]

for _ in range(N):
    w, v = map(int, input().split())
    ws.append(w)
    vs.append(v)

dp = [
    [0 for _ in range(M+1)]
    for _ in range(N+1)
]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = dp[i - 1][j]

        if j - ws[i] >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - ws[i]] + vs[i])

print(max(dp[N]))
