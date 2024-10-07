T = int(input())

# 0(up), 1(down), 2(left), 3(right)
dxs, dys = [-1,1,0,0],[0,0,-1,1]

def in_range(x,y):
    return 0 <= x <= n - 1 and 0 <= y <= n - 1

def convert(d):
    if d == "U":
        return 0
    elif d == "D":
        return 1
    elif d == "L":
        return 2
    else:
        return 3

def oppose_d(d):
    if d == "U":
        return "D"
    elif d == "D":
        return "U"
    elif d == "L":
        return "R"
    elif d == "R":
        return L

def move(x, y, d):
    global next_grid

    next_x, next_y = x + dxs[convert(d)], y + dys[convert(d)]

    if in_range(next_x, next_y):
        next_grid[next_x][next_y] = (next_grid[next_x][next_y][0] + 1, d)
    else:
        nd = oppose_d(d)
        next_grid[x][y] = (1, nd)

def move_all():
    global grid, next_grid

    next_grid = [
        [(0, 'U') for _ in range(n)]
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(n):
            if grid[i][j][0] == 1:
                move(i, j, grid[i][j][1])
    
    for i in range(n):
        for j in range(n):
            if next_grid[i][j][0] > 1:
                next_grid[i][j] = (0,"U")

    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]

for _ in range(T):
    n, m = map(int,input().split())

    grid = [
        [(0, 'U') for _ in range(n)]
        for _ in range(n)
    ]

    next_grid = [
        [(0, 'U') for _ in range(n)]
        for _ in range(n)
    ]
    
    for __ in range(m):
        x, y, d = input().split()
        x, y = int(x) - 1, int(y) - 1

        grid[x][y] = (1,d)
    
    for __ in range(n*2):
        move_all()


ans = 0

for i in range(n):
    for j in range(n):
        if grid[i][j][0] == 1:
            ans += 1

print(ans)