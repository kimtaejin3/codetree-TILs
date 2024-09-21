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
        # print(row)
        if row.count(0) > 0:
            row.remove(0)
            
            if dir == "R":
                row.insert(0, 0)
            else:
                row.append(0)

        grid[i] = row

elif dir == "U" or dir == "D":
    print(1)

for row in grid:
    for elem in row:
        print(elem, end=' ')
    print()