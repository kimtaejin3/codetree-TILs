n = int(input())
arr = list(map(int,input().split()))

cnt = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i < j < k and arr[i] < arr[j] < arr[k]:
                cnt += 1

print(cnt)