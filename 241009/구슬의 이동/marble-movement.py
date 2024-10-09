mapper = {
    "L": 0,
    "U": 1,
    "D": 2,
    "R": 3
}

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def reflect_marbles_on_grid():
    global grid, marbles

    for marble in marbles:
        r, c, d, v, n = marble
        grid[r][c] += 1

def remove_collision_marbles():
    global grid, marbles, k

    for i in range(n):
        for j in range(n):
            if grid[i][j] > k:
                for _ in range(grid[i][j] - k):
                    for marble in marbles:
                        if i == marble[0] and j == marble[1]:
                            marbles.remove(marble)
                            break


def move_all():
    global marbles

    dxs, dys = [0, -1, 1, 0], [-1, 0, 0, 1]
    new_marbles = []

    for marble in marbles:
        r, c, d, v, n = marble

        for _ in range(v):
            next_r, next_c = r + dxs[d], c + dys[d]

            if in_range(next_r, next_c):
                r, c = next_r, next_c

                next_next_r, next_next_c = r + dxs[d], c + dys[d]

                if not in_range(next_next_r, next_next_c):
                    d = 3 - d
        
        new_marbles.append((r, c, d, v, n))
    
    marbles = sorted(new_marbles, key = lambda x: (x[3], x[4]))
        
def simulate():
    global grid

    for i in range(n):
        for j in range(n):
            grid[i][j] = 0
    

    move_all()
    reflect_marbles_on_grid()
    remove_collision_marbles()

    

n, m, t, k = tuple(map(int, input().split()))

grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]

marbles = []


for i in range(1,m+1):
    r, c, d, v = tuple(input().split())
    marbles.append((int(r)-1, int(c)-1, mapper[d], int(v), i))


for _ in range(t):
    simulate()

print(len(marbles))