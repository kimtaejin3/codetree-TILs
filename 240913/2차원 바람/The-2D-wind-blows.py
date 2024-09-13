N, M, Q = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(N)]

for i in range(Q):
    r1,c1,r2,c2 = map(int,input().split())
    r1,c1,r2,c2 = r1-1,c1-1,r2-1,c2-1

    temp1 = grid[r1][c2]

    for i in range(c2,c1,-1):
        grid[r1][i] = grid[r1][i-1]

    temp2 = grid[r2][c2]
    for i in range(r2,r1,-1):
        grid[i][c2] = grid[i-1][c2]

    grid[r1+1][c2] = temp1

    temp3 = grid[r2][c1]
    for i in range(c1+1, c2):
        grid[r2][i-1] = grid[r2][i]

    grid[r2][c2-1] = temp2

    for i in range(r1, r2-1):
        grid[i][c1] = grid[i+1][c1]

    grid[r2-1][c1] = temp3

    ans = []

    for g in grid:
        ans.append(g.copy())

    dx,dy = [-1,1,0,0],[0,0,-1,1]

    def cal(x,y):
        s = []
        s.append(ans[x][y])
        for cx,cy in zip(dx,dy):
            nx,ny = x + cx, y + cy

            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                continue
            
            s.append(ans[nx][ny])
        
        return sum(s) // len(s)


    for x in range(r1,r2+1):
        for y in range(c1,c2+1):
            grid[x][y] = cal(x,y)

    for g in grid:
        for elem in g:
            print(elem, end=' ')
        print()