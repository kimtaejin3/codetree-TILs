s = input()
arr_s = s.replace("+","*").replace("-","*").split("*")
arr_s = list(set(arr_s))
n = len(arr_s)

choose = []

def get_value(opr):
    global choose
    index = -1
    
    for i in range(len(arr_s)):
        if arr_s[i] == opr:
            index = i

    return choose[index]

def calc(opr1, opr2, opt):
    opr1 = get_value(opr1)
    opr2 = get_value(opr2)

    if opt == "+":
        return opr1 + opr2
    elif opt == "*":
        return opr1 * opr2
    elif opt == "-":
        return opr1 - opr2

def calc_rest(val, opr2, opt):
    opr2 = get_value(opr2)

    if opt == "+":
        return val + opr2
    elif opt == "*":
        return val * opr2
    elif opt == "-":
        return val - opr2  

def calc_all():
    temp_s = s

    left_s = temp_s[0:3]
    temp_s = temp_s[3:]
    val = 0
    val = calc(left_s[0], left_s[2], left_s[1])

    while temp_s:
        left_s = temp_s[:2]
        temp_s = temp_s[2:]

        opt = left_s[0]
        opr = left_s[1]

        val = calc_rest(val,opr,opt)

    return val

ans = -1 

def func(idx, lev):
    global ans, choose

    if lev == n:
        ans = max(ans,calc_all())
        return
    
    for i in range(1,5):
        choose.append(i)
        func(i+1, lev + 1)
        choose.pop()

func(0, 0)

print(ans)