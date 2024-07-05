A = input()

ans = 0
for i in range(len(A)):
    for j in range(i+1, len(A)):
        if A[i] == '(' and A[j] == ')':
            ans += 1

print(ans)