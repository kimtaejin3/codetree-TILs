n, m, k = map(int, input().split())

grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

block = [
    1 for _ in range(m)
]

if n == 1:
    print(1)
    exit(0)

for row in range(n-1):
    flag = False
    for i in range(k-1, m+k-1):
        if grid[row+1][i] == 1:
            flag = True
    
    if flag:
        for i in range(k-1, m+k-1):
            grid[row][i] = 1
        break
    
for row in grid:
    for elem in row:
        print(elem, end=' ')
    print()