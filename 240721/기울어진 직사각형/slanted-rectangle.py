n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

ans = -1

ds = [(-1,1),(-1,-1),(1,-1),(1,1)]

for x in range(n):
    for y in range(n):
        cur_x, cur_y = x, y

        for a in range(1,n+1):
            for b in range(1,n+1):
                temp = 0
                flag = False

                for d in range(len(ds)):
                    if d%2 == 0:
                        for i in range(a):
                            temp += arr[cur_x][cur_y]
                            nx, ny = cur_x + ds[d][0], cur_y + ds[d][1]

                            if nx < 0 or nx > n - 1 or ny < 0 or ny > n-1:
                                flag = True
                                break
                            
                            cur_x, cur_y = nx, ny
                    else:
                        for i in range(b):
                            temp += arr[cur_x][cur_y]
                            nx, ny = cur_x + ds[d][0], cur_y + ds[d][1]

                            if nx < 0 or nx > n - 1 or ny < 0 or ny > n-1:
                                flag = True
                                break
                            
                            cur_x, cur_y = nx, ny
                    if flag:
                        break
                        
                        
                if flag:
                    continue        
                
                if temp == 26:
                    print(x, y)

                ans = max(ans, temp)

print(ans)