n, m = map(int, input().split())
arr = list(map(int, input().split()))
answer = []

ans = 0

def choose(lev, cnt):
    global ans 

    if lev == n:
        if cnt == m:
            val = 1
            for elem in answer:
                val = val | elem
            ans = max(val, ans)
        return

    answer.append(arr[lev])
    choose(lev+1, cnt+1)
    answer.pop()

    choose(lev+1, cnt)

choose(0,0)

print(ans)