n, m, r, c = map(int,input().split())
orders = input().split()

a = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 위(d[0]), 앞(d[1]), 오(d[2])
dice = [1,2,3]

r -= 1
c -= 1

def opposite_num(num):
    return 7 - num

a[r][c] = opposite_num(dice[0])

for i in range(m):
    order = orders[i]
    pre_up, pre_front, pre_right = dice[0],dice[1],dice[2]
    up, front, right = dice[0], dice[1], dice[2]

    nr, nc = r, c

    if order == "D":
        dice[0] = opposite_num(front)
        dice[1] = up
        nr += 1
        
    elif order == "U":
        dice[0] = front
        dice[1] = opposite_num(up)
        nr -= 1

    elif order == "L":
        dice[0] = right
        dice[2] = opposite_num(up)
        nc -= 1

    elif order == "R":
        dice[0] = opposite_num(right)
        dice[2] = up
        nc += 1
    
    if nr < 0 or nr > n - 1 or nc < 0 or nc > n - 1:
        dice[0] = pre_up
        dice[1] = pre_front
        dice[2] = pre_right
        continue
    
    
    r, c = nr, nc
    a[r][c] = opposite_num(dice[0])

ans = 0
for row in a:
    for elem in row:
        ans += elem

print(ans)