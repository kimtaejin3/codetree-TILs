OFFSET = 2000

N = OFFSET * 2
T = int(input())

direction_mapper = {
    'U': 0,
    'R': 1,
    'L': 2,
    'D': 3
}

def in_range(x, y):
    return 0 <= x <= N and 0 <= y <= N

def move_all():
    global marbles

    dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

    new_marbles = []

    for marble in marbles:
        x, y, w, n, d = marble

        next_x, next_y = x + dxs[d], y + dys[d]

        if in_range(next_x, next_y):
            new_marbles.append((next_x, next_y, w, n, d))

    marbles = new_marbles

next_marble_index = [
    [-1 for _ in range(N + 1)]
    for _ in range(N + 1)
]

for _ in range(T):

    n = int(input())
    marbles = []

    for i in range(n):
        x, y, w, d = input().split()
        marbles.append((int(x) * 2 + OFFSET, int(y) * 2 + OFFSET, int(w), i+1, direction_mapper[d]))
    
    ans = -1

    for i in range(0, N + 1):
        move_all()
        flag = False
 
        next_marbles = []

        for marble in marbles:
            x, y, w, n, d = marble

            if next_marble_index[x][y] == -1:
                next_marbles.append((x, y, w, n, d))
                next_marble_index[x][y] = len(next_marbles) - 1
            else:
                flag = True
                index = next_marble_index[x][y]
                tx, ty, tw, tn, td = next_marbles[index]
                if w > tw or (w == tw and n > tn):
                    next_marbles[index] = (tx, ty, tw, tn, td)

        marbles = next_marbles[:]

        for x, y, _, _, _ in next_marbles:
            next_marble_index[x][y] = -1
        
        next_marbles = []

        if flag:
            ans = i + 1

    print(ans)