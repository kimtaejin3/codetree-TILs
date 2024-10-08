n, m = map(int, input().split())

a = [
    [list() for _ in range(n)]
    for _ in range(n)
]

move_arr = []

for i in range(n):
    row = list(map(int, input().split()))

    for j in range(n):
        a[i][j].append(row[j])

nums = list(map(int,input().split()))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def get_pos(num):
    for i in range(n):
        for j in range(n):
            if num in a[i][j]:
                return (i, j)

def next_pos(x, y):
    dxs = [-1, -1, -1, 0, 1, 1, 1, 0]
    dys = [-1, 0, 1, 1, 1, 0, -1, -1]

    max_val, max_pos = -1, (-1, -1)

    for dx, dy in zip(dxs, dys):
        next_x, next_y = x + dx, y + dy

        if in_range(next_x, next_y) and len(a[next_x][next_y]) > 0 and max(a[next_x][next_y]) > max_val:
            max_val = max(a[next_x][next_y])
            max_pos = (next_x, next_y)

    return max_pos

def swap(pos1, pos2, num):
    move_arr = []

    x, y = pos1
    tx, ty = pos2

    popped = a[x][y].pop(0) 
    move_arr.append(popped)

    while popped != num:
        popped = a[x][y].pop(0)
        move_arr.append(popped)

    for i in range(len(move_arr)-1,-1,-1):
        a[tx][ty].insert(0,move_arr[i])


def simulate():
    for num in nums:
        x, y = get_pos(num)
        tx, ty = next_pos(x, y)
        if tx == -1 and ty == -1:
            continue
          
        swap((x,y), (tx,ty), num)

simulate()

for i in range(n):
    for j in range(n):
        if len(a[i][j]) == 0:
            print(None)
        else:
            print(' '.join(map(str,a[i][j])))