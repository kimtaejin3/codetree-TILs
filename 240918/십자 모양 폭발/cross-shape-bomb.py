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

print(positions)

for _ in range(1):
    for i in range(4):
        positions[i][0] += steps[i][0]
        positions[i][1] += steps[i][1]
    
    for position in positions:
        if 0 <= position[0] < n and 0 <= position[1] < n:
            grid[position[0]][position[1]] = 0

for row in grid:
    print(row)