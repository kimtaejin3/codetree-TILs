from collections import deque

NOT_EXISTS = (-1, -1)

n, k = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

r, c = tuple(map(int, input().split()))
curr_cell = (r - 1, c - 1)

q = deque()
visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y < n

def can_go(x, y, target_num):
    return in_range(x, y) and not visited[x][y] and \
           grid[x][y] < target_num

def initialize_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    curr_x, curr_y = curr_cell
    visited[curr_x][curr_y] = True
    q.append(curr_cell)

    target_num = grid[curr_x][curr_y]

    while q:
        curr_x, curr_y = q.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = curr_x + dx, curr_y + dy

            if can_go(new_x, new_y, target_num):
                q.append((new_x, new_y))
                visited[new_x][new_y] = True

def need_update(best_pos, new_pos):
    if best_pos == NOT_EXISTS:
        return True
    
    best_x, best_y = best_pos
    new_x, new_y = new_pos

    return (grid[new_x][new_y], -new_x, -new_y) > \
           (grid[best_x][best_y], -best_x, -best_y)

def move():
    global curr_cell

    initialize_visited()

    bfs()

    best_pos = NOT_EXISTS
    for i in range(n):
        for j in range(n):
            if not visited[i][j] or (i, j) == curr_cell:
                continue
            
            new_pos = (i, j)
            if need_update(best_pos, new_pos):
                best_pos = new_pos
    
    if best_pos == NOT_EXISTS:
        return False
    else:
        curr_cell = best_pos
        return True

for _ in range(k):
    is_moved = move()

    if not is_moved:
        break

final_x, final_y = curr_cell
print(final_x + 1, final_y + 1)