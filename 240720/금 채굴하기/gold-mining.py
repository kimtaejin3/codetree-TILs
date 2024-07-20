n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

def get_nums_of_gold(x,y,k):
    return sum([arr[i][j] for i in range(n) for j in range(n) if abs(x-i) + abs(y-j) <= k])


max_gold = 0

for x in range(n):
    for y in range(m):
        for k in range(n):

            num_of_gold = get_nums_of_gold(x,y,k)

            if num_of_gold * m >= k * k + (k+1) * (k+1):
                max_gold = max(max_gold, num_of_gold)

print(max_gold)