# 그룹으로 나눈다는 것을 어떻게 dp로 한다는지 모르겠다

n = int(input())
A = list(map(int, input().split()))

s = sum(A)
dp = [False] * (s)
dp[0] = True

for j in A:
    for i in range(s-1, 0, -1):
        if i - j < 0 or not dp[i - j]:
            continue
        dp[i] = True

ans = 100000

for i in range(1, s):
    if dp[i]:
        ans = min(ans, abs(s-i-i))

print(ans)
