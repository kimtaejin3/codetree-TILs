import sys

n = int(input())
a = list(map(int, input().split()))

choose = []

def isPossible():

    for i in range(1, len(choose)):
        if choose[i-1][0] + choose[i-1][1] < choose[i][1]:
            return False
    
    return True


ans = sys.maxsize

def search(lev):
    global ans

    if lev == n:
        if choose and choose[0][0] == a[0] and choose[-1][0] == a[-1] and isPossible():
            ans = min(ans, len(choose)-1)
        return

    choose.append((a[lev], lev))
    search(lev + 1)
    choose.pop()

    search(lev + 1)

search(0)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)