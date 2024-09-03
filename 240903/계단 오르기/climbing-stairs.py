n = int(input())

arr = [0] * (n+2)

arr[2] = 1
arr[3] = 1

for i in range(4, n):
    arr[i] = arr[i - 2] + arr[i - 3]


print(arr[n] % 10007)