OFFSET = 1000


T = int(input())

direction_mapper = {
    "U": 0,
    "L": 1,
    "R": 2,
    "D": 3,
}

def in_range(x, y):
    return 0 <= x <= 2000 and 0 <= y <= 2000

def move(x, y, w, n, d):
    global next_a, a
    is_collide = False

    dxs, dys = [-1, 0, 0, 1], [0, -1, 1, 0]

    next_x, next_y = x + dxs[d], y + dys[d]

    if in_range(next_x, next_y):
        # 중간에 충돌하는 경우 처리
        if (3-d) in a[next_x][next_y][2]:
            is_collide = True
            if w > a[next_x][next_y][0][0]:
                next_a[next_x][next_y].append((w, n, d))
            # n이 같을일은 없음.
            elif w == a[next_x][next_y][0][0] and n > a[next_x][next_y][1]:
                next_a[next_x][next_y].append((w, n, d))
        else:
            next_a[next_x][next_y].append((w, n, d))
    
    return is_collide

def detect_collision():
    is_collide = False

    for x in range(OFFSET * 2 + 1):
        for y in range(OFFSET * 2 + 1):
            if len(next_a[x][y]) > 1:
                next_a[x][y].sort(key = lambda x:(x[0],x[1]))
                popped = next_a[x][y][-1]
                next_a[x][y] = [popped]
                is_collide = True
    
    return is_collide


def move_all():
    global a
    is_collide = False

    for x in range(OFFSET * 2 + 1):
        for y in range(OFFSET * 2 + 1):
            for w, n, d in a[x][y]:

                flag = move(x, y, w, n, d)
                if flag:
                    is_collide = True
    
    return is_collide


for _ in range(T):
    a = [
        [[] for _ in range(OFFSET * 2 + 1)]
        for _ in range(OFFSET * 2 + 1)
    ]

    next_a = [
        [[] for _ in range(OFFSET * 2 + 1)]
        for _ in range(OFFSET * 2 + 1)
    ]

    N = int(input())

    for i in range(N):
        x, y, w, d = input().split()
        a[int(x) + OFFSET][int(y) + OFFSET].append((w, i+1, direction_mapper[d])) 
    
    ans = -1

    for i in range(OFFSET * 2 + 1, 2):
        next_a = [
            [[] for _ in range(OFFSET * 2 + 1)]
            for _ in range(OFFSET * 2 + 1)
        ]

        flag1 = move_all()
        flag2 = detect_collision()

        if flag1:
            ans = i + 2 - 1
        
        if flag2:
            ans = i + 2

        for x in range(OFFSET * 2 + 1):
            for y in range(OFFSET * 2 + 1):
                a[x][y] = next_a[x][y]