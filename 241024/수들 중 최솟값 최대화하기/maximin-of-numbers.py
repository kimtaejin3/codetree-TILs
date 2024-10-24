n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [False] * n
choose = []
ans = -1

def find_max(cnt):
    global ans

    if cnt == n:
        ans = max(min(choose), ans)
        return
    
    for i in range(n):
        if visited[i]:
            continue
        
        visited[i] = True
        choose.append(grid[cnt][i])
        find_max(cnt + 1)
        visited[i] = False
        choose.pop()

find_max(0)

print(ans)