N,M,K = map(int,input().split())

grid = [
    list(map(int,input().split()))
    for _ in range(N)
]

next_grid = [
    [0 for _ in range(N)]
    for _ in range(N)
]

def init_next_grid():
    for i in range(N):
        for j in range(N):
            next_grid[i][j] = 0

def rotate():
    init_next_grid()

    for i in range(N):
        for j in range(N):
            next_grid[i][j] = grid[N-j-1][i]
    
    for i in range(N):
        for j in range(N):
            grid[i][j] = next_grid[i][j]
    
def get_end_idx(start_idx, num):
    end_idx = start_idx
    
    for i in range(start_idx, N-1):
        if grid[i][num] == grid[i+1][num] and grid[i][num] != 0:
            end_idx += 1
        else:
            return end_idx

    if N == 1:
        return -1

    return N-1

def is_consecutive_exist():
    for col in range(N):
        for start_idx in range(N):
            end_idx = get_end_idx(start_idx,col)
            if end_idx < 0:
                return False
            if end_idx - start_idx + 1 >= M:
                return True
    
    return False

def bomb(num):
    for start_idx in range(N):
        end_idx = get_end_idx(start_idx, num)

        if end_idx - start_idx + 1 >= M:
            for i in range(start_idx, end_idx+1):
                grid[i][num] = 0

def down():
    init_next_grid()

    for i in range(N):
        next_row = N-1
        for j in range(N-1,-1,-1):
            if grid[j][i]:
                next_grid[next_row][i] = grid[j][i]
                next_row -= 1
        
    for i in range(N):
        for j in range(N):
            grid[i][j] = next_grid[i][j]


def bomb_all():
    init_next_grid()

    for i in range(N):
        bomb(i)

for _ in range(K):
    while is_consecutive_exist():
        bomb_all()
        down()
    rotate()
    down()

if is_consecutive_exist():
    bomb_all()
    down()

ans = 0

for row in grid:
    for elem in row: 
        if elem > 0:
            ans += 1
            
print(ans)