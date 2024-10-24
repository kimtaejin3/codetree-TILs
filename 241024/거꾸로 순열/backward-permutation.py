n = int(input())
visited = [False] * (n+1)

answer = []

def choose(lev):
    if lev == n:
        print(' '.join(map(str, answer)))
        return
    
    for i in range(n, 0, -1):
        if not visited[i]:
            answer.append(i)
            visited[i] = True
            choose(lev + 1)
            visited[i] = False
            answer.pop()

choose(0)