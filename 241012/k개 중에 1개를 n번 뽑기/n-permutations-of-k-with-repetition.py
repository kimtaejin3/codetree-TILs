K, N = map(int, input().split())
a = []

def choose(lev):
    if lev == N:
        print(' '.join(map(str,a)))
        return

    for i in range(1, K + 1):
        a.append(i)
        choose(lev + 1)
        a.pop()


choose(0)