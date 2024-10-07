T = int(input())

def in_range(x,y):
    return 0 <= x <= n - 1 and 0 <= y <= n - 1

mapper = {
    'U':0,
    'R':1,
    'L':2,
    'D':3
}

def move(x, y, d):
    dxs, dys = [-1, 0, 0, 1], [0, 1, -1, 0]
    global next_grid

    next_x, next_y = x + dxs[d], y + dys[d]

    if in_range(next_x, next_y):
        next_grid[next_x][next_y] = (next_grid[next_x][next_y][0] + 1, d)
    else:
        next_grid[x][y] = (next_grid[x][y][0] + 1, 3 - d)

def move_all():
    global grid, next_grid

    next_grid = [
        [(0, 0) for _ in range(n)]
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(n):
            if grid[i][j][0] == 1:
                move(i, j, grid[i][j][1])
    
    for i in range(n):
        for j in range(n):
            if next_grid[i][j][0] > 1:
                next_grid[i][j] = (0, 0)

    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]

for _ in range(T):
    n, m = map(int,input().split())

    grid = [
        [(0, 0) for _ in range(n)]
        for _ in range(n)
    ]

    for __ in range(m):
        x, y, d = input().split()
        x, y = int(x) - 1, int(y) - 1

        grid[x][y] = (1, mapper[d])
    
    for __ in range(n*2):
        move_all()

    ans = 0

    for i in range(n):
        for j in range(n):
            if grid[i][j][0] == 1:
                ans += 1

    print(ans)