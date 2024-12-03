n, s = input().split()
n = int(n)

arr = []
for _ in range(n):
    arr.append(input())

for i in range(n - 1, -1 , -1):
    if arr[i] == s:
        print(i)
        break


