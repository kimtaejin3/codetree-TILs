n = int(input())
c = []

for _ in range(n):
    c.append(tuple(map(int, input().split())))

dp = [0] * n

dp[0] = 1

for i in range(1, n):
    for j in range(i):
        if c[i][0] >= c[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

