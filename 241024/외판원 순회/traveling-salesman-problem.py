import sys

INT_MAX = sys.maxsize
n = int(input())
A = [
    [0]+ list(map(int, input().split()))
    for _ in range(n)
]

A.insert(0, [0 for _ in range(n+1)])

visited = [False] * (n + 1)
choose = []
ans = INT_MAX
def perm(lev):
    global ans
    if lev == n - 1:
        temp = A[1][choose[0]]
        for i in range(len(choose)-1):
            temp += A[choose[i]][choose[i+1]]
        temp += A[choose[-1]][1]

        ans = min(ans, temp)
        return
    
    for i in range(2, n + 1):
        if not visited[i]:
            visited[i] = True
            choose.append(i)
            perm(lev + 1)
            choose.pop()
            visited[i] = False
perm(0)
print(ans)