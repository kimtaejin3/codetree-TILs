n, m, t = tuple(map(int, input().split()))

grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

count = [
    [0 for _ in range(n)]
    for _ in range(n)
]

next_count = [
    [0 for _ in range(n)]
    for _ in range(n)
]

dxs, dys = [-1,1,0,0], [0,0,-1,1]

for _ in range(m):
    r, c = tuple(map(int,input().split()))
    count[r-1][c-1] = 1

def get_next_pos(r, c):
    
    next_pos = [r,c]
    max_val = grid[r][c]

    for dx, dy in zip(dxs, dys):
        nr, nc = r + dx, c + dy
        if nr < 0 or nr > n - 1 or nc < 0 or nc > n - 1:
            continue
        if grid[nr][nc] > max_val:
            max_val = grid[nr][nc]
            next_pos[0], next_pos[1] = nr, nc
    
    return (next_pos[0], next_pos[1])


def move_all():
    for i in range(n):
        for j in range(n):
            next_count[i][j] = 0
    
    for i in range(n):
        for j in range(n):
            if count[i][j]:
                nr, nc = get_next_pos(i,j)

                next_count[nr][nc] += 1

                if next_count[nr][nc] > 1:
                    next_count[nr][nc] = 0
    
    for i in range(n):
        for j in range(n):
            count[i][j] = next_count[i][j]

for _ in range(t+1):
    move_all()

ans = 0

for i in range(n):
    for j in range(n):
        if count[i][j]:
            ans += 1

print(ans)