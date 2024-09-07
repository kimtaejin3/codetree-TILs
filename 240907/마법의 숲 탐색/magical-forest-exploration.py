# 시뮬레이션을 통한 골렘을 좌표(배열)에 표시 
# 골렘들은 배열에 가지고 있고 위에서부터 아래로 한칸씩 이동 - 이때 검증이 들어감
# 골렘의 이동이 끝났으면 좌표 업데이트 (출구는 다른 값 넣기 ex. 출구는 2, 나머지는 1 이런식으로)
# 정령을 남쪽으로 이동시키는 시뮬레이션하기 - 이때도 검증 들어감

def adjustGrid(grid,x,y):
    for i in range(-1,2):
            if x+i <0 or x+i > R-1 or y-1<0 or y+1>C-1:
                continue
            
            if grid[x+i][y-1] > 0 or grid[x+i][y]>0 or grid[x+i][y+1]>0:
                return -1

            grid[x+i][y-1] = golrem[i+1][0]
            grid[x+i][y] = golrem[i+1][1]
            grid[x+i][y+1] = golrem[i+1][2]
    return grid

R, C, k = map(int,input().split())

grid = [
    [0]*C for _ in range(R)
]

golremsInfo = []

for _ in range(k):
    golremsInfo.append(tuple(list(map(int,input().split()))))

for i in range(k):
    c, d = golremsInfo[i]

    # 2는 골렘, 3은 출구
    golrem = [[0,1,0],[1,2,1],[0,1,0]]

    if d == 0:
        golrem[0][1] = 3
    elif d == 1:
        golrem[1][2] = 3
    elif d == 2:
        golrem[2][1] = 3
    elif d == 3:
        golrem[1][0] = 3
    
    x, y = 0, c - 1
    isLeft = True

    while True:
        nx = x + 1


        newGrid = adjustGrid(grid,nx,y)

        # 땅에 닿았거나 더 이상 이동할 수 없을 때
        if nx > R - 2:
            # grid = newGrid

            # for g in grid:
                # print(g)

            print('=== end ===')
            break
        
        if newGrid == -1:
            print("!!")
            if isLeft:
                y = y - 1
            else:
                y = y + 1
            if y < 0:
                y = 0
                isLeft = False
        else:
            x = nx
        
        print('move: ', x, y)