grid = [
    list(map(int,input().split())) for _ in range(4)
]

dir = input()

if dir == "R" or dir == "L":
    for i in range(4):
        row = grid[i].copy()

        while row.count(0) > 0:
            row.remove(0)
            
            if dir == "R":
                row.insert(0, -1)
            else:
                row.append(-1)

        for j in range(4):
            if row[j] == -1:
                row[j] = 0
  
        if dir == "L":
            for j in range(0, len(row)-1):
                if row[j] == row[j+1]:
                    row[j] += row[j+1]
                    row[j+1] = -1
        elif dir == "R":
            for j in range(len(row)-1, 0, -1):
                if row[j] == row[j-1]:
                    row[j] += row[j-1]
                    row[j-1] = -1

        while row.count(-1) > 0:
            row.remove(-1)

            if dir == "L":
                row.append(0)
            else:
                row.insert(0,0)
        grid[i] = row

elif dir == "U" or dir == "D":
    for i in range(4):
        col = []
        for j in range(4):
            col.append(grid[j][i])

        while col.count(0) > 0:
            col.remove(0)
            
            if dir == "D":
                col.insert(0, -1)
            else:
                col.append(-1)
        
        for j in range(4):
            if col[j] == -1:
                col[j] = 0

        if dir == "U":
            for j in range(0, len(col)-1):
                if col[j] == col[j+1]:
                    col[j] += col[j+1]
                    col[j+1] = -1
        elif dir == "D":
            for j in range(len(col)-1, 0, -1):
                if col[j] == col[j-1]:
                    col[j] += col[j-1]
                    col[j-1] = -1

        while col.count(-1) > 0:
            col.remove(-1)

            if dir == "U":
                col.append(0)
            else:
                col.insert(0,0)
                
        for j in range(4):
            grid[j][i] = col[j] 

for row in grid:
    for elem in row:
        print(elem, end=' ')
    print()