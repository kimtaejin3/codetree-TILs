OFFSET = 5

N = OFFSET * 2
T = int(input())

direction_mapper = {
    "U": 3,
    "L": 1,
    "R": 2,
    "D": 0,
}

def in_range(x, y):
    return 0 <= x <= N and 0 <= y <= N

def move_all():
    global marbles

    dxs, dys = [-1, 0, 0, 1], [0, -1, 1, 0]

    is_collide = False

    new_marbles = []
    for marble in marbles:
        x, y, w, n, d = marble

        next_x, next_y = x + dxs[d], y + dys[d]

        if in_range(next_x, next_y):
            flag = False

            for i in range(len(marbles)):
                tx,ty,tw,tn,td = marbles[i]

                if tx == next_x and ty == next_y and td == 3 - d:
                    if w < tw:
                        flag = True
                    elif w == tw and n < tn:
                        flag = True
            
            if not flag:
                # print('asdf')
                new_marbles.append((next_x, next_y, w, n, d))
    
    marbles = sorted(new_marbles, key = lambda x:(x[2], x[3]))

def detect_collision():
    global grid
    is_collide = False

    for x in range(N+1):
        for y in range(N+1):
            if grid[x][y] > 1:
                is_collide = True
                for _ in range(grid[x][y]-1):
                    for marble in marbles:
                        tx, ty, tw, tn, td = marble

                        if tx == x and ty == y:
                            marbles.remove(marble)
                            break
    
    return is_collide


for _ in range(T):
    grid = [
        [0 for _ in range(N + 1)]
        for _ in range(N + 1)
    ]

    n = int(input())
    marbles = []

    for i in range(n):
        x, y, w, d = input().split()
        marbles.append((int(y) + OFFSET, int(x) + OFFSET, int(w), i+1, direction_mapper[d]))
    
    ans = -1

    for i in range(0, OFFSET * 2 + 1, 2):
        for x in range(N+1):
            for y in range(N+1):
                grid[x][y] = 0
        
        # print('==')
        # print(marbles)
        flag1 = move_all()
        # print(marbles)
        # print('==')

        for marble in marbles:
            x, y, w, n, d = marble

            grid[y][x] += 1

        flag2 = detect_collision()
        if flag1:
            ans = i + 2 - 1
        
        if flag2:
            ans = i + 2

    print(ans)