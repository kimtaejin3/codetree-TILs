n = int(input())
grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def calc(x, y, move_dir):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    elapsed_time = 1

    while in_range(x, y):
        if grid[x][y] == 1:
            move_dir = 3 - move_dir
        elif grid[x][y] == 2:
            move_dir = (move_dir + 2) if move_dir < 2 else (move_dir - 2)
        
        x, y = x + dxs[move_dir], y + dys[move_dir]

        elapsed_time += 1
    
    return elapsed_time

ans = 0

for i in range(n):
    ans = max(ans, calc(n-1,i,0))
    ans = max(ans, calc(0,i,1))
    ans = max(ans, calc(i, n-1, 2))
    ans = max(ans, calc(i,0,3))

print(ans)