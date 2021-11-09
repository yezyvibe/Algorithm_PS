import sys
input = sys.stdin.readline
# 상 하 좌 우
dy = (-1, 1, 0, 0) # y축
dx = (0, 0, -1, 1) # x축 
dr = (3, 2, 0, 1)
dl = (2, 3, 1, 0)

for i in range(int(input())):
    x, y, d = 0, 0, 0
    max_x, max_y, min_x, min_y = 0, 0, 0, 0
    for order in input():
        print(order, x, y, d, '시작')
        if order == 'R':
            d = dr[d]
            print(d, 'R')
            continue
        elif order == 'L':
            d = dl[d]
            print(d, 'L')
            continue
        elif order == 'F':
            x += dx[d]
            y += dy[d]
        elif order == 'B':
            x -= dx[d]
            y -= dy[d]

        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    print(abs(max_x - min_x)*abs(max_y - min_y))