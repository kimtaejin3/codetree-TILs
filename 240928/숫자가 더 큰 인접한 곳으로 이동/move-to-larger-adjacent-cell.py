n, r, c = map(int,input().split())

grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

def inRange(x,y):
    return 0 <= x <= n-1 and 0 <= y <= n-1

dxs = [-1,1,0,1]
dys = [0,0,-1,1]

ans = []

def simulate(x,y):
    global ans

    cur_x, cur_y = x, y

    while True:
        max_pos = (0,0)
        max_val = grid[cur_x][cur_y]

        for dx, dy in zip(dxs,dys):
            next_x, next_y = cur_x + dx, cur_y + dy

            if inRange(next_x, next_y) and not visited[next_x][next_y] and grid[next_x][next_y] > max_val:
                max_val = grid[next_x][next_y]
                visited[next_x][next_y] = True
                max_pos = next_x,next_y
        
        if max_val == grid[cur_x][cur_y]:
            break
        ans.append(grid[max_pos[0]][max_pos[1]])
        cur_x, cur_y = max_pos


simulate(r,c)
print(ans)