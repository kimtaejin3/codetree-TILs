n = int(input())
dp = [0] * (n + 1)
nums = [1, 2, 5]

dp[1] = 1
dp[2] = 1
dp[5] = 1

for i in range(2, n + 1):
    for j in range(len(nums)):
        if i - nums[j] >= 0:
            dp[i] += dp[i - nums[j]]

print(dp[n] % 10007)
