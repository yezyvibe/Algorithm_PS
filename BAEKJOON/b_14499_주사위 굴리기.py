n, m, x, y, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
directions = list(map(int, input().split()))
# 동 서 북 남
d = {1:[0,1], 2:[0,-1], 3:[-1,0], 4:[1,0]}
dice = [0]*7

for dir in directions:
    dx, dy = d[dir][0], d[dir][1]
    # 다음 이동 좌표 구하기
    x += dx
    y += dy

    # 지도 밖을 벗어나지 않는지 확인
    if 0<= x < n and 0<= y < m:

        # 동서북남 탐색
        if dir == 1:
            dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
        elif dir == 2:
            dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
        elif dir == 3:
            dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
        else:
            dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]

        # 이동칸에 쓰여 있는 값이 0, 0아닌 값에 따라 처리
        if arr[x][y] == 0:
            arr[x][y] = dice[6]
        else:
            dice[6] = arr[x][y]
            arr[x][y] = 0
        print(dice[1])

    # 인덱스 에러
    else:
        x -= dx
        y -= dy
