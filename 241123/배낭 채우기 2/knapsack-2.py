N, M = map(int, input().split())
ws = [0]
vs = [0]

dp = [-1] * (M + 1)
dp[0] = 0

for _ in range(N):
    w, v = map(int, input().split())
    ws.append(w)
    vs.append(v)

for i in range(1, M + 1):
    for j in range(1, N + 1):
        if i - ws[j] >= 0:
            dp[i] = max(dp[i], dp[i - ws[j]] + vs[j])

print(max(dp))


