import sys
INT_MAX = sys.maxsize

n, m = map(int, input().split())
A = list(map(int, input().split()))

dp = [INT_MAX] * (m + 1)

dp[0] = 0

for i in range(len(A)):
    for j in range(m, -1, -1):
        if j - A[i] >= 0:
            dp[j] = min(dp[j], dp[j - A[i]] + 1)

if dp[m] == INT_MAX:
    print('No')
else:
    print('Yes')
