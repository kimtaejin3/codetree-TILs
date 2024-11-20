n, m = map(int, input().split())
A = list(map(int, input().split()))

choose = []

ans = 'No'

def find(lev):
    global ans

    if lev == n:
        if sum(choose) == m:
            ans = 'Yes'
        
        return

    choose.append(A[lev])
    find(lev + 1)
    choose.pop()
    find(lev + 1)

find(0)

print(ans)
