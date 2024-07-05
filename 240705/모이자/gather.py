import sys

n = int(input())

house = list(map(int,input().split()))
ans = sys.maxsize
for i in range(len(house)):
    target = i
    total_distance = 0

    for j in range(len(house)):
        total_distance += house[j] * abs(i-j)
    
    ans = min(ans, total_distance)
    
print(ans)