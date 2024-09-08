N,M,Q = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(N)]
visited = [False] * N

def shift(r,d):
    if d == "R":
        temp = grid[r][0]
        for i in range(0,M-1):
            grid[r][i] = grid[r][i+1]
        grid[r][-1] = temp
    elif d == "L":
        temp = grid[r][-1]
        for i in range(M-1,0,-1):
            grid[r][i] = grid[r][i-1]
        grid[r][0] = temp

def checkUp(r):
    if r < 1:
        return False
    for i in range(M):
        if grid[r-1][i] == grid[r][i]:
            return True
    return False

def checkDown(r):
    if r > N - 2:
        return False

    for i in range(M):
        if grid[r+1][i] == grid[r][i]:
            return True
    return False

def operate(r,d):
    if visited[r]:
        return

    shift(r,d)
    visited[r] = True

    if checkUp(r):
        if d == "L":
            operate(r-1,"R")
        elif d == "R":
            operate(r-1,"L")

    if checkDown(r):
        if d == "L":
            operate(r+1,"R")
        elif d == "R":
            operate(r+1,"L")

for _ in range(Q):
    r,d = input().split()
    r = int(r) - 1
    operate(r,d)

for g in grid:
    for elem in g:
        print(elem, end=' ')
    print()