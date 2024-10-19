n, m, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))
choose = []
# print(arr)
def calc():
    # print(choose)
    a = [1 for _ in range(n+1)]
    
    for i in range(len(choose)):
        a[choose[i]] += arr[i+1]

    cnt = 0

    for el in a:
        if el >= m:
            cnt += 1
    
        
    return cnt

ans = 0

def f(lev):
    global ans
    if lev == n:
        ans = max(ans, calc())
        return
    
    for i in range(1, k+1):
        choose.append(i)
        f(lev + 1)
        choose.pop()


f(0)
print(ans)