# dp로도 풀어보기
from collections import deque

N = int(input())
visited = [False for _ in range(1000001)]

if N == 1:
    print(0)
    exit(0)

def bfs():
    q = deque([(N, 1)])
    visited[N] = True

    while q:
        num, depth = q.popleft()

        for i in range(4):
            next_num = -1

            if i == 0:
                next_num = num + 1
            elif i == 1:
                next_num = num - 1
            elif i == 2 and num % 2 == 0:
                next_num = num // 2
            elif i == 3 and num % 3 == 0:
                next_num = num // 3
            else:
                continue 

            if not visited[next_num]:
                visited[next_num] = True

                if visited[1]:
                    print(depth)
                    exit(0)
                q.append((next_num, depth + 1))
            

bfs()