n, t = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

for _ in range(t):
    temp1 = A[-1]
    temp2 = B[-1]
    temp3 = C[-1]

    for i in range(n-1,0,-1):
        A[i] = A[i-1]

    for i in range(n-1,0,-1):
        B[i] = B[i-1]
    
    for i in range(n-1,0,-1):
        C[i] = C[i-1]
    A[0] = temp3
    B[0] = temp1
    C[0] = temp2

for elem in A:
    print(elem, end=' ')
print()

for elem in B:
    print(elem, end=' ')
print()

for elem in C:
    print(elem, end=' ')
print()