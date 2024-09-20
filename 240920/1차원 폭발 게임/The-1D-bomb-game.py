n, m = map(int, input().split())

arr = []
for _ in range(n):
    val = int(input())
    arr.append(val)

# 포인터 2개쓰기

def find():
    global arr
    start, end = 0, 1
    
    while end < len(arr):
        if arr[start] == arr[end]:
            end += 1
        else:
            if end - start >= m:
                for i in range(start, end):
                    arr[i] = -1
            start = end
    
    if end - start >= m:
        for i in range(start, end):
            arr[i] = -1

    while arr.count(-1) > 0:
        arr.remove(-1)

def isExist():
    global arr
    cnt = 0
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            cnt += 1
    
    return cnt


while isExist() + 1 >= m:
    find()


print(len(arr))
for elem in arr:
    print(elem)