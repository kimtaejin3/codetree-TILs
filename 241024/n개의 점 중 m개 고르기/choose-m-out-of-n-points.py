import sys

INT_MAX = sys.maxsize

n, m = tuple(map(int, input().split()))
points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
selected_points = list()

ans = INT_MAX

def dist(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

def calc():
    return max([
        dist(p1, p2)
        for i, p1 in enumerate(selected_points)
        for j, p2 in enumerate(selected_points)
        if i != j
    ])

def find_min(idx, cnt):

    if cnt == m:
        ans = min(ans, calc())
        return
    
    if idx == n:
        return

    selected_points.append(points[idx])
    find_min(idx + 1, cnt + 1)
    selected_points.pop()

    find_min(idx + 1, cnt)