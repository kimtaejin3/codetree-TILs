n, m = tuple(map(int,input().split()))

a = [
    list(map(int,input().split()))
    for _ in range(n)
]

dxs, dys = [-1,-1,-1,0,1,1,1,0],[-1,0,1,1,1,0,-1,-1]

def in_range(x, y):
    return 0 <= x <= n - 1 and 0 <= y <= n - 1

def get_pos(num):
    for i in range(n):
        for j in range(n):
            if a[i][j] == num:
                return (i,j)


def find_pos_max_val(x,y):
    max_val = 0
    max_pos = (0,0)

    for dx, dy in zip(dxs, dys):
        next_x, next_y = x + dx, y + dy

        if in_range(next_x, next_y) and a[next_x][next_y] > max_val:
            max_val = a[next_x][next_y]
            max_pos = (next_x, next_y)

    return max_pos

def swap(x,y):
    tx, ty = find_pos_max_val(x,y)

    temp = a[x][y]
    a[x][y] = a[tx][ty]
    a[tx][ty] = temp


for i in range(m):
    for num in range(1, n * n + 1):
        x, y = get_pos(num)
        swap(x,y)

for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()