n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

# 4개와 2개
block01 = [
    [
        [1,0],
        [1,1],
    ],
    [
        [0,1],
        [1,1],
    ],
     [
        [1,1],
        [0,1],
    ],
     [
        [1,1],
        [1,0],
    ],
]

block02 = [
    [
        [1,0,0],
        [1,0,0],
        [1,0,0]
    ],
    [
        [1,1,1],
        [0,0,0],
        [0,0,0]
    ]
]

ans = -1 

for x in range(n):
    for y in range(m):
        
        block01_sum = -1
        block02_sum = -1

        # block 1
        for d in range(4):
            temp = 0
            for k in range(x, x+2):
                for l in range(y, y+2):
                    if(k > n - 1 or k < 0 or l > m - 1 or l < 0):
                        continue
                    temp += arr[k][l] * block01[d][k-x][l-y]
            
            block01_sum = max(block01_sum,temp)

        # block 2
        for d in range(2):
            temp = 0
            for k in range(x, x+3):
                for l in range(y, y+3):
                    if k > n - 1 or k < 0 or l > m - 1 or l < 0: 
                        continue
                    temp += arr[k][l] * block02[d][k-x][l-y]
            
            block02_sum = max(block02_sum, temp)

        ans = max(ans, block01_sum, block02_sum)

print(ans)