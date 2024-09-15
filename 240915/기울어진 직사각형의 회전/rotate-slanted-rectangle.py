n = int(input())

grid = [list(map(int,input().split())) for _ in range(n)]
r,c,m1,m2,m3,m4,d = map(int,input().split())

rectangle = []

dxs = [-1,-1,1,1]
dys = [1,-1,-1,1]

tries_count = [m1, m2, m3, m4]
tr,tc = r-1, c-1
rectangle.append(grid[tr][tc])

def inRange(r,c):
    return 0 <= r < n and 0 <= c < n 

for i in range(len(tries_count)):
    count = tries_count[i]
    for j in range(count):
        tr, tc = tr + dxs[i], tc + dys[i]
        if inRange(tr,tc):
            rectangle.append(grid[tr][tc])

rectangle.pop()

if d == 0:
    temp = rectangle.pop()
    rectangle.insert(0,temp)
elif d == 1:
    temp = rectangle.pop(0)
    rectangle.append(temp)

tr, tc = r - 1, c - 1
grid[tr][tc] = rectangle[0]
index = 1

for i in range(len(tries_count)):
    count = tries_count[i]
    for j in range(count):
        tr, tc = tr + dxs[i], tc + dys[i]
        if inRange(tr,tc) and index < len(rectangle):
            grid[tr][tc] = rectangle[index]
            index += 1

for row in grid:
    for elem in row:
        print(elem, end=' ')
    print()