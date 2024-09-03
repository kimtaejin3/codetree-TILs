def fibo(n):
    if n <= 2:
        return 1
    
    if memo[n] > 0:
        return memo[n]

    memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

n = int(input())
memo = [-1] * (n+1)
print(fibo(n))