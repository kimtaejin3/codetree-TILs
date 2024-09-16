n = int(input())

arr = []

for _ in range(n):
    arr.append(int(input()))

s1, e1 = map(int,input().split())

tmp = []

for i in range(len(arr)):
    if s1-1 <= i <= e1-1:
        continue
    
    tmp.append(arr[i])

arr = tmp.copy()
tmp = []

s2, e2 = map(int,input().split())
for i in range(len(arr)):
    if s2-1 <= i <= e2-1:
        continue
    
    tmp.append(arr[i])


print(len(tmp))
for elem in tmp:
    print(elem)