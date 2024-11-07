MAX_N = 1000

memo = [-1] * (MAX_N + 1)

def climb(N):
    if N == 2 or N == 3:
        return 1
    
    if memo[N] != -1:
        return memo[N]
    
    memo[N] = (climb(N - 2) + climb(N - 3)) % 10007

    return memo[N]

n = int(input())
ans = climb(n)
print(ans)