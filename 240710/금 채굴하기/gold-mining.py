# 1부터 n-1까지 채굴영역 만들기 (n-1 이 맞으려나? -> 맞는거 같다! 아니면 고치면 되지)
# 채굴영역의 가운데를 각각의 셀에 맞추기 (반복문)
# 손해계산하고 업데이트 하기

# 생각해볼점
# 그러면 채굴영역을 어떻게 만들까?
# 사실 가운데 고정시켜놓고 k값을 알 수 있으니 거리계산을 해서 알아낼 수 있기는함.

# 채굴액자를 n * n 으로 만들어 놓기 -> 왜? 일단 배열은 만들어 놓아야 하니 그 틀을 최대 기준으로 잡는 것임

# 63%에서 틀림 -> mining area의 center position을 어떻게 잡아야 할지가 이슈
# -> 그래서 center position을 완전탐색 했더니 시간초과가 났다.

n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

def generateMiningArea(k, center_x, center_y):
    mining_area = [[0] * n for _ in range(n)]
    
    mining_area[center_x][center_y] = 1

    for x in range(n):
        for y in range(n):
            if k >= abs(x-center_x) + abs(y-center_y):
                mining_area[x][y] = 1

    return mining_area

ans = 0

for k in range(n):
    if n % 2 == 0:
        for center_x in range(n//2-1, n//2+1):
            for center_y in range(n//2-1, n//2+1):

                mining_area = generateMiningArea(k,center_x,center_y)

                for x in range(n):
                    for y in range(n):
                        temp = 0
                        for i in range(x-center_x, x-center_x+n):
                            for j in range(y-center_y, y-center_y+n):
                                if i<0 or i>n-1 or j<0 or j>n-1:
                                    continue
                                
                                temp += mining_area[i+center_x-x][j+center_y-y] * arr[i][j]

                        if k * k + (k+1) * (k+1) <= m * temp:
                            ans = max(ans, temp)
    else:
        center_x = n//2
        center_y = n//2
        mining_area = generateMiningArea(k,center_x,center_y)

        for x in range(n):
            for y in range(n):
                temp = 0
                for i in range(x-center_x, x-center_x+n):
                    for j in range(y-center_y, y-center_y+n):
                        if i<0 or i>n-1 or j<0 or j>n-1:
                            continue
                        
                        temp += mining_area[i+center_x-x][j+center_y-y] * arr[i][j]

                if k * k + (k+1) * (k+1) <= m * temp:
                    ans = max(ans, temp)

            
print(ans)

'''
0 0 0 0 0 0
0 0 0 0 0 0 
0 0 0 0 0 0 
0 0 0 0 0 0
0 0 0 0 0 0 
0 0 0 0 0 0 
'''