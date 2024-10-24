import sys
import math

INT_MAX = sys.maxsize

n, m = map(int, input().split())

arr = []
ans = INT_MAX
for _ in range(n):
    arr.append(tuple(map(int, input().split())))

candidate = []

def get_dis(a, b):
    ax, ay = a
    bx, by = b

    return int(math.pow(abs(ax-bx),2) + math.pow(abs(ay - by),2))

def choose(lev, cnt):
    global ans
    if cnt == m:
        # here
        temp = -1

        for i in range(len(candidate)):
            for j in range(len(candidate)):
                if i == j:
                    continue

                temp = max(temp, get_dis(candidate[i], candidate[j]))

        # print(temp)
        ans = min(ans, temp)
        return
    if lev == n:
        return

    candidate.append(arr[lev])
    choose(lev + 1, cnt + 1)
    candidate.pop()

    choose(lev + 1, cnt)

choose(0, 0)
print(ans)