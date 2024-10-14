n = int(input())

a = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

a = sorted(a, key = lambda x:x[1])

ans = 1

last = a[0][1]

for i in range(1, len(a)):
    if last < a[i][0]:
        last = a[i][1]
        ans += 1

print(ans)