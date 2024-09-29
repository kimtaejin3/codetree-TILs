n = int(input())
a = []

for _ in range(n):
    a.append(int(input()))

ans = 0

for sea_height in range(1, max(a)):
    count = 0
    is_concecutive = False
    for elem in a:
        if elem > sea_height:
            count += 0
            is_concecutive = False
        else:
            if is_concecutive:
                continue
            count += 1
            is_concecutive = True
    
    ans = max(ans, count)

print(ans+1)