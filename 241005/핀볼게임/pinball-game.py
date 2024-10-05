n = int(input())

a = [
    [0] + list(map(int,input().split())) + [0]
    for _ in range(n)
]

a.insert(0, [0 for _ in range(n+2)])
a.append([0 for _ in range(n+2)])

scaled_n = n + 2

dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

elapsed_time = 0

ans = -1

def get_d(i,j):
    if i == 0:
        return 0
    elif j == 0:
        return 2
    elif i == scaled_n - 1:
        return 1
    elif j == scaled_n - 1:
        return 3

def move():
    global x, y, d, elapsed_time

    while True:
        elapsed_time += 1
        x, y = x + dxs[d], y + dys[d]
        if x < 1 or x >= scaled_n - 1 or y < 1 or y >= scaled_n - 1:
            break

        if a[x][y] == 1:
            if d == 0:
                d = 3
            elif d == 1:
                d = 2
            elif d == 2:
                d = 1
            elif d == 3:
                d = 0

        elif a[x][y] == 2:
            if d == 0:
                d = 2
            elif d == 1:
                d = 3
            elif d == 2:
                d = 0
            elif d == 3:
                d = 1
        

for i in range(scaled_n):
    for j in range(scaled_n):
        if (i == 0 or j == 0 or i == scaled_n - 1 or j == scaled_n - 1):
            if (i == 0 and j == 0) or (i == 0 and j == scaled_n - 1) or (i == scaled_n -1 and j == scaled_n -1) and (i==scaled_n -1 and j == 0):
                continue
            elapsed_time = 0
            x, y = i, j
            d = get_d(i, j)
            move()
            ans = max(ans, elapsed_time)


print(ans)