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

    dxs, dys = [-0.5, 0, 0, 0.5], [0, -0.5, 0.5, 0]

    new_marbles = dict()

    for marble in marbles:
        if marbles[marble]:
            continue

        x, y, w, n, d = marble

        next_x, next_y = x + dxs[d], y + dys[d]

        if in_range(next_x, next_y):
            new_marbles[(next_x, next_y, w, n, d)] = False

    marbles = new_marbles

for _ in range(T):

    n = int(input())
    marbles = dict()

    for i in range(n):
        x, y, w, d = input().split()
        marbles[(int(y) + OFFSET, int(x) + OFFSET, int(w), i+1, direction_mapper[d])] = False
    
    ans = -1

    for i in range(0, N + 1):
        move_all()
        flag = False
        grid = {}

        for marble in marbles:
            if marbles[marble]:
                continue

            x, y, w, n, d = marble

            if not (x,y) in grid:
                grid[(x,y)] = (w, n, d)
            else:
                flag = True
                tw, tn, td = grid[(x,y)]
                if w > tw or (w == tw and n > tn):
                    grid[(x,y)] = (w, n, d)

                    marbles[(x,y,tw,tn,td)] = True
                else:
                    grid[(x,y)] = (tw, tn, td)

                    marbles[(x, y, w, n, d)] = True
        
        if flag:
            ans = i + 1

    print(ans)