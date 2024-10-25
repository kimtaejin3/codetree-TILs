n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]
people = 0


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(x, y):
    global people

    dxs, dys = [1, -1, 0, 0],[0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == 1:
            visited[nx][ny] = True
            people += 1
            dfs(nx, ny)

towns = 0
peoples = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            towns += 1
            people = 1
            visited[i][j] = True
            dfs(i, j)

            peoples.append(people)


print(towns)
for people in sorted(peoples):
    print(people)