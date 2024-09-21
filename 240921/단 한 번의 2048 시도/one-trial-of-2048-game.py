grid = [
    list(map(int,input().split())) for _ in range(4)
]

dir = input()

if dir == "R" or dir == "L":
    for i in range(4):
        row = grid[i].copy()

        for j in range(3,0,-1):
            if row[j] == row[j-1] and row[j] != 0:
                row[j] += row[j-1]
                row[j-1] = 0

        if row.count(0) > 0:
            row.remove(0)
            
            if dir == "R":
                row.insert(0, 0)
            else:
                row.append(0)

        grid[i] = row

elif dir == "U" or dir == "D":
    for i in range(4):
        col = []
        for j in range(4):
            col.append(grid[j][i])

        for j in range(3,0,-1):
            if col[j] == col[j-1] and col[j] != 0:
                col[j] += col[j-1]
                col[j-1] = 0

        while col.count(0) > 0:
            col.remove(0)
            
            if dir == "D":
                col.insert(0, -1)
            else:
                col.append(-1)
        
        for j in range(4):
            if col[j] == -1:
                col[j] = 0

        for j in range(4):
            grid[j][i] = col[j] 

for row in grid:
    for elem in row:
        print(elem, end=' ')
    print()