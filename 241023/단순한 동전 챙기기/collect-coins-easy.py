import sys
n = int(input())

grid = [
    list(input())
    for _ in range(n)
]

nums = []

def get_idx():
    start = -1
    end = -1

    for x in range(n):
        for y in range(n):
            if grid[x][y] == 'S':
                start = (x,y)
            elif grid[x][y] == 'E':
                end = (x,y)
            elif grid[x][y].isnumeric():
                nums.append((int(grid[x][y]),(x,y)))
    
    return start, end

choose = []
start_idx, end_idx = get_idx()

def get_dis(a, b):
    x1, y1 = a
    x2, y2 = b

    return abs(x1 - x2) + abs(y1 - y2)

def get_dis_all(arr):

    d1 = get_dis(start_idx, arr[0][1])
    d2 = get_dis(arr[0][1], arr[1][1])
    d3 = get_dis(arr[1][1], arr[2][1])
    d4 = get_dis(arr[2][1], end_idx)

    return d1 + d2 + d3 + d4

ans = sys.maxsize

def f(index, lev):
    global ans
    if lev == 3:
        candidate = choose[:]
        candidate.sort()
        ans = min(get_dis_all(candidate[:]), ans)
        return
    
    for i in range(index, len(nums)):
        choose.append(nums[i])
        f(i+1, lev + 1)
        choose.pop()

f(0,0)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)