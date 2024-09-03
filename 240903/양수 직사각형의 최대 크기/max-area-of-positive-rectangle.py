n,m = map(int,input().split())

grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

def isAllPositiveNumbers(x,y,w,h):
    
    isAllPositiveNumbers = True

    for i in range(x, x+h):
        for j in range(y, y+w):
            if i > n-1 or j > m-1:
                isAllPositiveNumbers = False
                break
            if grid[i][j] <= 0:
                isAllPositiveNumbers = False
                break
    
    return isAllPositiveNumbers

ans = -1

for x in range(n):
    for y in range(m):
        for w in range(1,m+1):
            for h in range(1,n+1):
                if isAllPositiveNumbers(x,y,w,h):
                    ans = max(ans, w*h)

print(ans)