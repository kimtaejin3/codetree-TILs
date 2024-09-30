n = int(input())
x, y = map(int, input().split())

grid = [
    list(input())
    for _ in range(n)
]

dxs = [0,-1,0,1]
dys = [1,0,-1,0]

d = 0

# while True? => 무한루프 
# 무한루프인데 -1을 판단하는 기준? 가본 곳에 도착했으면 -1 출력 후, break!!
# 종료조건을 모르겠음. visited 방식도 특정 케이스를 커버하지는 못함
# 딱 아래의 케이스 : if visited[][] 부분을 어떻게 핸들할지 모르겠음

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

def can_go(d):
    ans = False
    if d == 0:
        if x+1>n-1:
            return False
        return grid[x+1][y] == "#"
    elif d == 1:
        if y+1 > n-1:
            return False
        return grid[x][y+1] == "#"
    elif d == 2:
        if x-1 < 0:
            return False
        return grid[x-1][y] == "#"
    elif d == 3:
        if y-1<0:
            return False
        return grid[x][y-1] == "#"

    return ans

def is_collision(d):
    ans = False
    if d == 0:
        if y + 1 > n-1:
            return False
        return grid[x][y+1] == "#"
    elif d == 1:
        if x -1 < 0:
            return False
        return grid[x-1][y] == "#"
    elif d == 2:
        if y-1 < 0:
            return False
        return grid[x][y-1] == "#"
    elif d == 3:
        if x+1 > n-1:
            return False
        return grid[x+1][y] == "#"

    return ans

t = 0

x -= 1
y -= 1

visited[x][y] = True

while True:
    t += 1

    if can_go(d):

        while is_collision(d):
            d = (d+1)%4

        x = x + dxs[d]
        y = y + dys[d]
        
        if x < 0 or x > n - 1 or y < 0 or y > n - 1:
            break
        if visited[x][y]:
            print('ㅋㅋ:',(x,y))
            print(-1)
            exit(0)
        visited[x][y] = True

    else:
        
        d -= 1
        if d < 0:
            d = 3
        
        x = x + dxs[d]
        y = y + dys[d]

        if visited[x][y]:
            print(-1)
            exit(0)

        visited[x][y] = True
    
    print((x,y))

print(t)