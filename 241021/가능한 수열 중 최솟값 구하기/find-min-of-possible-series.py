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
        if not check() and not ans:
            ans = ''.join(map(str, choose))
        return

    for i in range(len(nums)):
        choose.append(nums[i])
        func(lev + 1)
        choose.pop()

func(0)
print(ans)