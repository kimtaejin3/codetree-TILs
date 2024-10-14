n = int(input())

a = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

choose = []
ans = 0

def func(index, lev, length):
    global ans

    if lev == length:
        ans = max(ans, length)
        return


    for i in range(index, n):
        if (not choose) or choose[-1][1] < a[index][0]:
            choose.append(a[index])
            func(i+1, lev+1, length)
            choose.pop()


for i in range(1, n+1):
    func(0, 0, i)

print(ans)