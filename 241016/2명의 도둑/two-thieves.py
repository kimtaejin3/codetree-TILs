n, m, c = tuple(map(int, input().split()))

a = [
    list(map(int, input().split()))
    for _ in range(n)
]

b = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def fill(row, col):
    if sum(b[row][col:col+m]) > 0:
        return False

    for i in range(col, col + m):
        b[row][i] = 1

    return True
    
def remove_fill(row, col):
    for i in range(col, col + m):
        if i > n - 1:
            break

        b[row][i] = 0

def cal():
    temp = 0
    for i in range(n):
        cnt = 0
        s = []
        for j in range(n):
            if b[i][j] == 1:
                s.append(a[i][j])
                cnt += 1

                while sum(s) > c:
                    s.sort()
                    s.pop(0)
            
            if cnt == m:
                for i in range(len(s)):
                    temp += s[i] * s[i]
                cnt = 0
                s = []
    
    return temp

ans = -1

def func(lev):
    global ans
    if lev == 2:
        ans = max(ans, cal())
        return

    for i in range(n):
        for j in range(n - m + 1):
            can_fill = fill(i, j)

            if can_fill:
                func(lev + 1)
                remove_fill(i, j)

func(0)
print(ans)