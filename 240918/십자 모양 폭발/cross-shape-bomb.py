n = int(input())

grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

r, c = map(int, input().split())

val = grid[r-1][c-1] 
grid[r-1][c-1] = 0

steps = [(-1,0),(1,0),(0,-1),(0,1)]
positions = [[r-1,c-1] for _ in range(4)]

for _ in range(val - 1):
    for i in range(4):
        positions[i][0] += steps[i][0]
        positions[i][1] += steps[i][1]
    
    for position in positions:
        if 0 <= position[0] < n and 0 <= position[1] < n:
            grid[position[0]][position[1]] = 0

for i in range(n):
    for j in range(n-1, 0, -1):
        if grid[j][i] == 0:
            k = j - 1

            while k >= 0 and grid[k][i] == 0:
                k = k - 1
            
            if k >= 0:
                grid[j][i] = grid[k][i]
                grid[k][i] = 0

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()