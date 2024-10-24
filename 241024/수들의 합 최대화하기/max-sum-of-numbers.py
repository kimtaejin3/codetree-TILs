n = int(input())

a = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [False] * (n + 1)
answer = []
ans = - 1

def func(lev):
    global ans

    if lev == n:
        ans = max(ans, sum(answer))
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            answer.append(a[lev][i])
            func(lev + 1)
            visited[i] = False
            answer.pop()


func(0)
print(ans)