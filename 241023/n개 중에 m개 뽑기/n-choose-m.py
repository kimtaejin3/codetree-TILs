n, m = map(int, input().split())

answer = []

def choose(index, lev):

    if lev == m:
        print(' '.join(map(str,answer)))
        return
    
    for i in range(index+1, n+1):
        answer.append(i)
        choose(i, lev+1)
        answer.pop()

choose(0, 0)