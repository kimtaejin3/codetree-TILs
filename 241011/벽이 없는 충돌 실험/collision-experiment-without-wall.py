OFFSET = 2000
N = OFFSET * 2

# 방향 매핑
direction_mapper = {
    "U": 3,
    "L": 1,
    "R": 2,
    "D": 0,
}

def in_range(x, y):
    return 0 <= x <= N and 0 <= y <= N

def move_all():
    global marbles

    # 이동 방향에 따른 변화량 (0.5 단위로 움직임)
    dxs, dys = [-0.5, 0, 0, 0.5], [0, -0.5, 0.5, 0]
    
    new_marbles = dict()

    for marble in marbles:
        if marbles[marble]:
            continue  # 이미 충돌한 구슬은 무시

        x, y, w, n, d = marble
        next_x, next_y = x + dxs[d], y + dys[d]

        if in_range(next_x, next_y):
            new_marbles[(next_x, next_y, w, n, d)] = False

    marbles = new_marbles

# 테스트 케이스 입력 처리
T = int(input())

for _ in range(T):
    n = int(input())
    marbles = dict()

    for i in range(n):
        x, y, w, d = input().split()
        marbles[(int(y) + OFFSET, int(x) + OFFSET, int(w), i+1, direction_mapper[d])] = False
    
    ans = -1

    # 최대 N번 반복
    for i in range(0, N + 1):
        move_all()  # 구슬 이동
        flag = False
        grid = {}

        # 구슬 충돌 체크
        for marble in marbles:
            if marbles[marble]:
                continue  # 이미 충돌한 구슬은 무시

            x, y, w, n, d = marble

            if not (x, y) in grid:
                grid[(x, y)] = (w, n, d)  # 구슬 위치 기록
            else:
                flag = True  # 충돌 발생
                tw, tn, td = grid[(x, y)]

                # 더 강한 구슬이 남아야 함
                if w > tw or (w == tw and n > tn):
                    grid[(x, y)] = (w, n, d)
                    marbles[(x, y, tw, tn, td)] = True  # 약한 구슬 충돌 처리
                else:
                    marbles[(x, y, w, n, d)] = True  # 현재 구슬 충돌 처리
        
        if flag:
            ans = i + 1  # 충돌이 발생한 시점 기록

    print(ans)