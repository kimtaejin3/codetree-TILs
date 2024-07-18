n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

ans = -1

for x in range(n):
    for y in range(n):
        cur_x, cur_y = x, y
        for a in range(1,n+1):
            for b in range(1,n+1):

                temp = 0
                flag = False
                
                # 여기에 for문 4개
                for i in range(a+1):
                    temp += arr[cur_x][cur_y]

                    nx, ny = cur_x - 1, cur_y + 1
                    
                    if nx < 0 or ny > n-1:
                        flag = True
                        break
                    
                    cur_x, cur_y = nx, ny

                if flag: 
                    break

                for i in range(b+1):
                    temp += arr[cur_x][cur_y]

                    nx, ny = cur_x - 1, cur_y - 1
                    
                    if nx < 0 or ny < 0:
                        flag = True
                        break
                    
                    cur_x, cur_y = nx, ny
                if flag: 
                    break
                for i in range(a+1):
                    temp += arr[cur_x][cur_y]

                    nx, ny = cur_x + 1, cur_y - 1
                    
                    if nx > n-1 or ny < 0:
                        flag = True
                        break
                    
                    cur_x, cur_y = nx, ny

                if flag: 
                    break

                for i in range(b+1):
                    temp += arr[cur_x][cur_y]

                    nx, ny = cur_x + 1, cur_y + 1
                    
                    if nx > n-1 or ny > n-1:
                        flag = True
                        break
                    
                    cur_x, cur_y = nx, ny
               
                ans = max(ans, temp)

print(ans)