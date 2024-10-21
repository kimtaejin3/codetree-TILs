n = int(input())

nums = [4, 5, 6]

choose = []

def check():
    s = ''.join(map(str, choose))

    for k in range(1, n//2+1):
        for i in range(len(s)-1):
            if i+k*2 > n:
                continue
            print('s:',s)
            print('temp:',s[i:i+k], s[i+k:i+k*2])
            if s[i:i+k] == s[i+k: i+k*2]:
                return True

    return False

ans = ''

def func(lev):
    global ans
    
    if lev == n:
        print('choose:',choose)
        return

    for i in range(len(nums)):
        choose.append(nums[i])
        if len(choose) == 1 or not check():
            func(lev + 1)
        choose.pop()

func(0)