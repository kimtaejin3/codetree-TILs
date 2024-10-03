n, m, r, c = map(int,input().split())

a = [
    [0 for _ in range(n)]
    for _ in range(n)
]

r -= 1
c -= 1

a[r][c] = 1

dxs, dys = [-1,1,0,0],[0,0,-1,1]

judge = [1]

for t in range(1,m+1):
    for i in range(n):
        for j in range(n):
            if a[i][j] in judge:
                top = (i + dxs[0] * t, j + dys[0] * t)
                bottom = (i + dxs[1] * t, j + dys[1] * t)
                left = (i + dxs[2] * t, j + dys[2] * t)
                right = (i + dxs[3] * t, j + dys[3] * t)

                if top[0] >= 0 and a[top[0]][top[1]] not in judge:
                    a[top[0]][top[1]] = t + 1
                
                if bottom[0] < n and a[bottom[0]][bottom[1]] not in judge:
                    a[bottom[0]][bottom[1]] = t + 1
                
                if left[1] >= 0 and a[left[0]][left[1]] not in judge:
                    a[left[0]][left[1]] =  t + 1
                
                if right[1] < n and a[right[0]][right[1]] not in judge:
                    a[right[0]][right[1]] =  t + 1
    
    judge.append(t + 1)

ans = 0

for row in a:
    for elem in row:
        if elem > 0:
            ans += 1

print(ans)