# 배열을 입력으로 받고 연속 수열인지 판단하는 함수
# 다 완성은 했지만 더 나은 해결책이 있으려나
def isHappySequence(datas,m):
    
    for i in range(len(datas)):
        target = datas[i]
        cnt = 0
        lastPosition = -1 
        for j in range(len(datas)):
            if (target == datas[j] and (abs(j-lastPosition) == 1 or lastPosition == -1)):
                cnt += 1
                lastPosition = j
            elif target == datas[j]:
                cnt = 0
        
        if cnt >= m:
            return True

    return False

n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

# 또 하나의 고민 세로 배열 추출을 어떻게 하면 좋을까

# 일단은 가로 배열들부터 해결해보자

ans = 0

for a in arr:
    if isHappySequence(a,m):
        ans += 1


# 일단 제일 먼저 생각나는 방법으로 세로 배열들을 구해보자
for i in range(n):
    tempArr = []
    for j in range(n):
        tempArr.append(arr[j][i])
    
    if isHappySequence(tempArr,m):
        ans += 1

print(ans)

# -- 기록 --
# 틀렸는데 아마 isHappySequence에 문제가 있지 않을까