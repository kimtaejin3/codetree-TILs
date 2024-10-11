n, m, t = tuple(map(int, input().split()))

mapper = {
    "U": 0,
    "L": 1,
    "R": 2,
    "D": 3,
}

grid = [
    [-1 for _ in range(n)]
    for _ in range(n)
]

marbles = []
next_marbles = []

for i in range(m):
    x, y, d, w = input().split()

    marbles.append((int(x)-1, int(y)-1, mapper[d], int(w), i+1))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move(marble):
    x, y, d, w, n = marble

    dxs, dys = [-1,0,0,1],[0,-1,1,0]

    next_x, next_y = x + dxs[d], y + dys[d]
    next_d = d

    if not in_range(next_x, next_y):
        next_d = 3 - d
        next_x, next_y = x, y 

    return next_x, next_y, next_d, w, n

def move_all():
    global marbles

    next_marbles = []

    for marble in marbles:
        x, y, d, w, n = move(marble)

        if grid[x][y] == -1:
            next_marbles.append((x, y, d, w, n))
            grid[x][y] = len(next_marbles) - 1
        else:
            index = grid[x][y]
            tx, ty, td, tw, tn = next_marbles[index]
            new_w, new_d, new_n = w + tw, d if n > tn else td, n if n > tn else tn
            
            next_marbles[index] = (x, y, new_d, new_w, new_n)
    
    for x, y, _, _, _ in next_marbles:
        grid[x][y] = -1
    
    marbles = next_marbles[:]

def simulate():
    move_all()

for _ in range(t):
    simulate()

marbles.sort(key = lambda x:x[3])

print(len(marbles), marbles[-1][3])