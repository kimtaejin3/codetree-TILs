import sys

COIN_NUM = 9
INT_MAX = sys.maxsize

n = int(input())
m = 3

grid = [
    input()
    for _ in range(n)
]

coin_pos = list()
selected_pos = list()

start_pos = (-1, -1)
end_pos = (-1, -1)

ans = INT_MAX

def dist(a, b):
    (ax, ay), (bx, by) = a, b
    return abs(ax - bx) + abs(ay - by)

def calc():
    num_moves = dist(start_pos, selected_pos[0])
    for i in range(m - 1):
        num_moves += dist(selected_pos[i], selected_pos[i+1])
    num_moves += dist(selected_pos[m - 1], end_pos)

    return num_moves

def find_min_moves(curr_idx, cnt):
    global ans

    if cnt == m:
        ans = min(ans, calc())
        return
    
    if curr_idx == len(coin_pos):
        return
    
    find_min_moves(curr_idx + 1, cnt)

    selected_pos.append(coin_pos[curr_idx])
    find_min_moves(curr_idx + 1, cnt + 1)
    selected_pos.pop()

for i in range(n):
    for j in range(n):
        if grid[i][j] == 'S':
            start_pos = (i, j)
        if grid[i][j] == 'E':
            end_pos = (i, j)

for num in range(1, COIN_NUM + 1):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == str(num):
                coin_pos.append((i, j))

find_min_moves(0, 0)

if ans == INT_MAX:
    ans = -1

print(ans)