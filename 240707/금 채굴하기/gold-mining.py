# 1부터 n-1까지 채굴영역 만들기 (n-1 이 맞으려나? -> 맞는거 같다! 아니면 고치면 되지)
# 채굴영역의 가운데를 각각의 셀에 맞추기 (반복문)
# 손해계산하고 업데이트 하기

# 생각해볼점
# 그러면 채굴영역을 어떻게 만들까?
# 사실 가운데 고정시켜놓고 k값을 알 수 있으니 거리계산을 해서 알아낼 수 있기는함.

# 채굴액자를 n * n 으로 만들어 놓기 -> 왜? 일단 배열은 만들어 놓아야 하니 그 틀을 최대 기준으로 잡는 것임

n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

def generateMiningArea(k):
    mining_area = [[0] * n for _ in range(n)]
    center_x = n // 2 
    center_y = n // 2

    mining_area[center_x][center_y] = 1

    for x in range(n):
        for y in range(n):
            if k >= abs(x-center_x) + abs(y-center_y):
                mining_area[x][y] = 1

    return mining_area

ans = -1

for s in range(1,n):
    mining_area = generateMiningArea(s)

    center_x = n // 2
    center_y = n // 2

    for x in range(n):
        for y in range(n):
            diff_x = abs(x-center_x)
            diff_y = abs(y-center_y)
            temp = 0
            for i in range(x-diff_x, x-diff_x+n):
                for j in range(y-diff_y, y-diff_y+n):
                    if i<0 or i>n-1 or j<0 or j>n-1:
                        continue
                    
                    temp += mining_area[i-x+diff_x][j-y+diff_y] * arr[i][j]
                 
            if s * s + (s+1) * (s+1) <= m * temp:
                ans = max(ans, temp)
            

print(ans)