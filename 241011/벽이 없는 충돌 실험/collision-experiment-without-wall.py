OFFSET = 2000

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
                    is_collide = True
                    if w < tw:
                        flag = True
                    elif w == tw and n < tn:
                        flag = True
            
            if not flag:
                new_marbles.append((next_x, next_y, w, n, d))

    marbles = new_marbles
    return is_collide

for _ in range(T):
    grid = {}

    n = int(input())
    marbles = []

    for i in range(n):
        x, y, w, d = input().split()
        marbles.append((int(y) + OFFSET, int(x) + OFFSET, int(w), i+1, direction_mapper[d]))
    
    ans = -1

    for i in range(0, N + 1, 2):
        
        flag1 = move_all()
        flag2 = False

        for marble in marbles:
            x, y, w, n, d = marble

            if not (x,y) in grid:
                grid[(x,y)] = (w, n, d)
            else:
                flag2 = True
                tw, tn, td = grid[(x,y)]
                if w > tw or (w == tw and n > tn):
                    grid[(x,y)] = (w, n, d)
                    marbles.remove((x, y, tw, tn, td))
                else:
                    grid[(x,y)] = (tw, tn, td)
                    marbles.remove((x, y, w, n, d))

        
        if flag1:
            ans = i + 2 - 1
        
        if flag2:
            ans = i + 2

    print(ans)