n, s = input().split()
n = int(n)

arr = []
for _ in range(n):
    arr.append(input())

for i in range(n):
    if arr[i] == s:
        print(i)
        break


