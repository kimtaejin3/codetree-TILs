obj = {
    "N": [1,0],
    "E": [0,1],
    "S": [-1,0],
    "W": [0,-1]
}

n = int(input())
cur = [0,0]
for _ in range(n):
    d, count = input().split()
    count = int(count)

    x,y = obj[d]

    for i in range(count):
        cur[0] += x
        cur[1] += y

print(cur[1], cur[0])