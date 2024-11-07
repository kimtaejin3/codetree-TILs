def fibo(N):
    global memo

    if N <= 2:
        return 1
    
    if memo[N] != -1:
        return memo[N]
    
    return fibo(N - 1) + fibo(N - 2)

N = int(input())
memo = [-1] * (N + 1)

ans = fibo(N)

print(ans)