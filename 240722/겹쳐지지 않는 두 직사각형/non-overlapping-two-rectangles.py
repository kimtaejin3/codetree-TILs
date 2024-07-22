import sys
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
ans = -sys.maxsize
for x1 in range(n):
    for y1 in range(m):
        for w1 in range(m+1):
            for h1 in range(n+1):
                for x2 in range(n):
                    for y2 in range(m):
                        for w2 in range(m+1):
                            for h2 in range(n+1):
                                if y1 <= y2 <=y1+h1 and x1 <= x2 <= x1+w1:
                                   
                                    continue
                                if x1 + w1 > m-1 or y1 + h1 > n-1 or x2 + w2 > m-1 or y2 + h2 > n-1:
                                   
                                    continue

                                temp = 0

                                for i in range(x1,x1+w1+1):
                                    for j in range(y1, y1+h1+1):
                                        temp += arr[i][j]
                                
                                for i in range(x2,x2+w2+1):
                                    for j in range(y2, y2+h2+1):
                                        temp += arr[i][j]
                            
                                ans = max(ans, temp)

print(ans)