n, t = map(int,input().split())
belt = [list(map(int,input().split())) for _ in range(2)]

for _ in range(t):
    temp1 = belt[0][-1]
    belt[0].pop()

    temp2 = belt[1][-1]
    belt[1].pop()

    belt[0].insert(0,temp2)
    belt[1].insert(0,temp1)

for b in belt:
    for e in b:
        print(e,end=' ')
    print()