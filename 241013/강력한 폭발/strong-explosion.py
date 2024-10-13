n = int(input())

a = [
    list(map(int,input().split()))
    for _ in range(n)
]

next_a = [
    [0 for _ in range(n)]
    for _ in range(n)
]

bomb_cnt = 0
bombs = []
for x in range(n):
    for y in range(n):
        if a[x][y]:
            bombs.append([x,y,1])
            bomb_cnt += 1

def explode(x, y, k):
    next_a[x][y] = 1

    if k == 1:

        for i in range(2):
            next_x, next_y = x - i - 1, y

            if next_x > -1:
                next_a[next_x][next_y] = 1
            
        
        for i in range(2):
            next_x, next_y = x + i + 1, y

            if next_x < n:
                next_a[next_x][next_y] = 1

    elif k == 2:

        up = x - 1, y
        down = x + 1, y
        left = x, y - 1
        right = x, y + 1

        if up[0] > -1:
            next_a[up[0]][up[1]] = 1
        if down[0] < n:
            next_a[down[0]][down[1]] = 1
        if left[1] > -1:
            next_a[left[0]][left[1]] = 1
        if right[1] < n:
            next_a[right[0]][right[1]] = 1

    elif k == 3:
        one = x - 1, y - 1
        two = x - 1, y + 1
        three = x + 1, y - 1
        four = x + 1, y + 1

        if one[0] > -1 and one[1] > -1:
            next_a[one[0]][one[1]] = 1
        if two[0] > -1 and two[1] < n:
            next_a[two[0]][two[1]] = 1
        if three[0] < n and three[1] > -1:
            next_a[three[0]][three[1]] = 1
        if four[0] < n and four[1] < n:
            next_a[four[0]][four[1]] = 1

def explode_all():
    for bomb in bombs:
        x, y, k = bomb
        if a[x][y] > 0:
            explode(x, y, k)

ans = 0

def func(lev):
    global ans
    # base case
    if lev == bomb_cnt:
        explode_all()
        cnt = 0
        for x in range(n):
            for y in range(n):
                cnt += next_a[x][y]

        ans = max(ans, cnt)

        for x in range(n):
            for y in range(n):
                next_a[x][y] = 0
        return

    # recursive case
    
    for k in range(1, 4):
        bombs[lev][2] = k
        func(lev + 1)

func(0)

print(ans)