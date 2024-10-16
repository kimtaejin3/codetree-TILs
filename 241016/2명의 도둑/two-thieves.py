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

new_s = []
temp_s = []
max_val = -1
def get_new_s(s, lev):
    global new_s, max_val, new_s
    if lev == len(s):
        if sum(temp_s) <= c:
            if max_val < sum(temp_s):
                max_val = sum(temp_s)
                new_s = temp_s[:]
        return

    temp_s.append(s[lev])
    get_new_s(s, lev + 1)

    temp_s.pop()
    get_new_s(s, lev + 1)


def cal():
    global new_s, temp_s, max_val

    temp = 0
    for i in range(n):
        cnt = 0
        s = []
        for j in range(n):
            if b[i][j] == 1:
                s.append(a[i][j])
                cnt += 1

            if cnt == m:
                # 41 ~ 43이 문제임
                # while sum(s) > c:
                #     s.sort()
                #     s.pop(0)
                get_new_s(s, 0)
                
                # print(new_s)

                # 으아!!!! maxVal 말고 새로운 s 넘어오게....
                # print(max_val)
                for i in range(len(new_s)):
                    temp += new_s[i] * new_s[i]
                # print(s)
                cnt = 0
                s = []
                new_s, temp_s = [], []
                max_val = -1
    
    return temp

ans = -1

def func(lev):
    global ans
    if lev == 2:
        # print(cal())
        ans = max(ans, cal())
        # print('==')
        return

    for i in range(n):
        for j in range(n - m + 1):
            can_fill = fill(i, j)

            if can_fill:
                func(lev + 1)
                remove_fill(i, j)

func(0)
print(ans)