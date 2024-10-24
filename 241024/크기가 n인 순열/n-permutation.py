n = int(input())

visited = [False] * (n + 1)
answer = []

def choose(lev):
    if lev == n:
        print(' '.join(map(str,answer)))
        return

    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            answer.append(i)
            choose(lev + 1)
            visited[i] = False
            answer.pop()


choose(0)