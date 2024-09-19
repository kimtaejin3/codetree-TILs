n, m = map(int, input().split())

arr = []
for _ in range(n):
    val = int(input())
    arr.append((val, False))

# 포인터 2개쓰기

def find():
    c = 1
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            c += 1
        else:
            c = 1

        if c > m - 1:
            return (arr[i],i,c)


print(find())