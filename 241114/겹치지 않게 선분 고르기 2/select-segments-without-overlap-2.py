#그리디
n = int(input())

c = []
for _ in range(n):
    c.append(tuple(map(int, input().split())))

c.sort(key = lambda x : (x[1], x[0]))

cnt = 1

s, e = c[0]

for i in range(1, len(c)):
    s_t, e_t = c[i]

    if s_t > e:
        e = e_t
        cnt += 1

print(cnt)

