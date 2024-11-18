import sys

INT_MAX = sys.maxsize

n, m = map(int, input().split())
A = list(map(int, input().split()))

# dp[M]: 원소의 합이 M이 되는 A의 최소 수열 길이
dp = [INT_MAX] * (m + 1)

dp[0] = 0

for i in range(len(A)):
    for j in range(m, -1, -1):
        if j - A[i] >= 0:
            dp[j] = min(dp[j], dp[j - A[i]] + 1)

if dp[m] == INT_MAX:
    print(-1)
else:
    print(dp[m])




