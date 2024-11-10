n = int(input())

num = [
    [0] + list(map(int, input().split()))
    for _ in range(n)
]

num.insert(0, [0 for _ in range(n + 1)])

dp = [
    [1 for _ in range(n + 1)]
    for _ in range(n + 1)
]

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(x, y):
    return 1 <= x < n + 1 and 1 <= y < n + 1

for x in range(1, n+1):
    for y in range(1, n+1):
        for dx, dy in zip(dxs, dys):
            prev_x, prev_y = x + dx, y + dy

            if in_range(prev_x, prev_y):
                if num[prev_x][prev_y] < num[x][y]:
                    dp[x][y] = max(dp[prev_x][prev_y] + 1, dp[x][y])


# for row in dp:
#     for elem in row:
#         print(elem, end=' ')
#     print()

ans = -1 
for x in range( n+1):
    for y in range( n+1):
        ans = max(ans, dp[x][y])

print(ans)