import sys

n, m = map(int, input().split())

a = []
choose = []
origin = []

for i in range(m):
    a.append(tuple(map(int, input().split())))

def move(col, arr, ans):

    pos = (1, col)

    x, y = pos[0], pos[1]

    while x <= 15:
        if (y, x) in arr:
            y += 1
        elif (y-1, x) in arr:
            y -= 1
        
        x += 1
    
    ans.append(y)

ans = sys.maxsize

def simulate(arr):
    ans = []
    for i in range(n):
        move(i+1, arr, ans)
    return ans[:]

origin = simulate(a)

def func(index, lev, n):
    global ans 

    if lev == n:
        temp = simulate(choose)

        if temp == origin:
            ans = min(ans, lev)

        return False
    
    for i in range(index, m):
        choose.append(a[i])
        func(i + 1, lev + 1, n)
        choose.pop()

for i in range(m+1):
    func(0, 0, i)

print(ans)