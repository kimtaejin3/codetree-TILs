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

while t < 100:
    t += 1

    if can_go(d):

        if is_collision(d):
            d = (d+1)%4

        x = x + dxs[d]
        y = y + dys[d]

        if x < 0 or x > n - 1 or y < 0 or y > n - 1:
            break

    else:
        d -= 1
        if d < 0:
            d = 3
        
        x = x + dxs[d]
        y = y + dys[d]
    
    # print((x,y), can_go(d))
print(t)
   

# print(grid)