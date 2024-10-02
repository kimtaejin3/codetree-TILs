n, m, r, c = map(int,input().split())
orders = input().split()

a = [
    [0 for _ in range(n)]
    for _ in range(n)
]

up, front, right = 1, 2, 3

r -= 1
c -= 1

def opposite_num(num):
    return 7 - num

a[r][c] = opposite_num(up)

for i in range(m):
    order = orders[i]
    pre_up, pre_front, pre_right = up, front, right
    temp_up, temp_front, temp_right = up, front, right

    nr, nc = r, c

    if order == "D":
        up = opposite_num(temp_front)
        front = temp_up
        nr += 1
        
    elif order == "U":
        up = temp_front
        front = opposite_num(temp_up)
        nr -= 1

    elif order == "L":
        up = temp_right
        right = opposite_num(temp_up)
        nc -= 1

    elif order == "R":
        up = opposite_num(temp_right)
        right = temp_up
        nc += 1
    
    if nr < 0 or nr > n - 1 or nc < 0 or nc > n - 1:
        up = pre_up
        front = pre_front
        right = pre_right
        continue
    
    
    r, c = nr, nc
    a[r][c] = opposite_num(up)

ans = 0
for row in a:
    for elem in row:
        ans += elem

print(ans)