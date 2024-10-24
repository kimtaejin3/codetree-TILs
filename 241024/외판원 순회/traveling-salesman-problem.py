import sys

INT_MAX = sys.maxsize

n = int(input())

cost = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [False] * n
picked = []

ans = INT_MAX

def find_min(cnt):
    global ans

    if cnt == n:
        total_cost = 0
        for i in range(n-1):
            curr_cost = cost[picked[i]][picked[i + 1]]
            if curr_cost == 0:
                return
            
            total_cost += curr_cost

        additional_cost = cost[picked[-1]][0]
        if additional_cost == 0:
            return
        
        ans = min(ans, total_cost + additional_cost)
        return
    
    for i in range(n):
        if visited[i]:
            continue
        
        visited[i] = True
        picked.append(i)

        find_min(cnt + 1)

        visited[i] = False
        picked.pop()

visited[0] = True
picked.append(0)
find_min(1)
print(ans)