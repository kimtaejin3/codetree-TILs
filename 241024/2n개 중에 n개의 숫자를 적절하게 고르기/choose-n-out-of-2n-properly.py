import sys

INT_MAX = sys.maxsize

n = int(input())

arr = list(map(int, input().split()))

arr_sum = sum(arr)

choose = []

ans = INT_MAX

def comb(lev, cnt):
    global ans

    if cnt == n:
        ans = min(ans, abs(arr_sum - sum(choose)*2))
        return

    if lev == n*2:
        return
    
    choose.append(arr[lev])
    comb(lev + 1, cnt + 1)
    choose.pop()

    comb(lev + 1, cnt)

comb(0,0)
print(ans)