n, m, k = map(int, input().split())

a = [
    [0 for _ in range(n+1)]
    for _ in range(n+1)
]

def in_range(x,y):
    return 1 <= x <= n and 1 <= y <= n

def get(d):
    if d == "R":
        return (0,1)
    elif d == "L":
        return (0,-1)
    elif d == "U":
        return (-1,0)
    elif d == "D":
        return (1,0)

apple = []
commands = []

for _ in range(m):
    x, y = tuple(map(int,input().split()))
    a[x][y] = 2


elapsed_time = 0

x, y = 1,1
snake = [[1,1]]
ds = []

for _ in range(k):
    d, p = input().split()
    p = int(p)

    ds.append(d)
    dx, dy = get(d)
    past_d = ds[len(ds)-2]

    x, y = snake[0][0], snake[0][1]

    is_game_over = False

    for i in range(p):
        elapsed_time += 1
        
        x, y = x + dx, y + dy

        if not in_range(x,y):
            is_game_over = True
            break
        
       
        snake.insert(0, [x,y])

            
        if a[x][y] == 2:
            a[x][y] = 0

        else:
            snake.pop()
            if snake.count([x,y]) > 1:
                is_game_over = True
                break
            
    
    if is_game_over:
        break


print(elapsed_time)