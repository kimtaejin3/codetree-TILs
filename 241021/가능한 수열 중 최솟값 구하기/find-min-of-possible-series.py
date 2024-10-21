n = int(input())

nums = [4, 5, 6]

choose = []

def check():
    s = ''.join(map(str, choose))

    for k in range(1, n//2+1):
        for i in range(n-1):
            if i+k*2 > n:
                continue
            if s[i:i+k] == s[i+k: i+k*2]:
                return True

    return False

ans = ''

def func(lev):
    global ans

    if lev == n:
        if not check():
            ans = ''.join(map(str, choose))
            print(ans)

            #이렇게 하니까 20%까지는 갔음.
            #다 구해놓고 하는 방식이 아니라 조건에 맞지 않을시 재귀를 하면 안될 것 같음.
            exit(0)
        return

    for i in range(len(nums)):
        choose.append(nums[i])
        func(lev + 1)
        choose.pop()

func(0)