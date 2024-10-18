k, n = map(int, input().split())

choose = []
def func(lev):
    if lev == n:
        print(' '.join(map(str,choose)))
        return
    
    for i in range(1, k+1):
        if lev == 0 or lev == 1 or not (choose[lev-2] == i and choose[lev-1] == i and choose[lev-1] == choose[lev-2]):
            choose.append(i)
            func(lev + 1)
            choose.pop()

func(0)