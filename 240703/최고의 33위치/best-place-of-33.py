n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

ans = -1
for i in range(n):

    for j in range(n):
        cnt = 0

        for k in range(i+3):
            for l in range(j+3):
                if k > n-1 or l > n-1:
                    continue
                cnt += arr[k][l]
    
        ans = max(ans, cnt)


print(ans)