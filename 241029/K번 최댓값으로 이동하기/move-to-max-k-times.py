from collections import deque

n, k = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]
r, c = map(int, input().split())
r, c = r - 1, c - 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def find_max_pos(pos):

    q = deque([pos])
    curr_num = grid[pos[0]][pos[1]]
    max_poses = []
    moves = []
    max_num = -1
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if in_range(nx, ny) and grid[nx][ny] < curr_num and not visited[nx][ny]:
                visited[nx][ny] = True
                # print(grid[nx][ny], end=' ')
                moves.append((grid[nx][ny], (nx, ny)))
                if max_num <= grid[nx][ny]:
                    max_num = grid[nx][ny]
                    # max_poses.append((nx, ny))

                q.append((nx, ny))

    for m in moves:
        num, pos = m
        if num == max_num:
            max_poses.append(pos)

    if len(max_poses) == 0:
        return (-1, -1)
    else:
        return sorted(max_poses)[0]


pre_r, pre_c = r, c
ans_r, ans_c = -1, -1

for _ in range(k):
    new_r, new_c = find_max_pos((pre_r, pre_c))
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    if new_r == -1 and new_c == -1:
        ans_r, ans_c = pre_r, pre_c
        break
    else:
        pre_r, pre_c = new_r, new_c
        ans_r, ans_c = new_r, new_c

print(ans_r + 1, ans_c + 1)