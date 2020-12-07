import sys
from collections import deque


def snake(d):
    dir = 1  # 방향
    x, y = 0, 0  # 뱀위치
    answer = 1  # 시간
    q = deque([(x, y)])
    bg[x][y] = 2
    d = deque(d)
    t_x, c = d.popleft()
    while True:
        nx, ny = x + dx[dir], y + dy[dir]
        if 0 <= nx < n and 0 <= ny < n and bg[nx][ny] != 2:
            if bg[nx][ny] != 1:
                tmp_x, tmp_y = q.popleft()
                bg[tmp_x][tmp_y] = 0  # 꼬리 자르기
            bg[nx][ny] = 2
            x, y = nx, ny
            q.append((nx, ny))
            if answer == int(t_x):
                dir = change_direction(dir, c)
                if d:
                    t_x, c = d.popleft()
            answer += 1
        else:
            return answer


# 상우하좌
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]


def change_direction(x, c):
    # 상우하좌
    if c == 'L':
        x = (x - 1) % 4
    else:
        x = (x + 1) % 4
    return x


input = sys.stdin.readline
n = int(input())
k = int(input())
bg = [[0] * n for _ in range(n)]
for i in range(k):  # 사과 표시
    a, b = map(int, input().rstrip().split(' '))
    bg[a - 1][b - 1] = 1
# for b in bg:
    # print(b)
d = [input().rstrip().split(' ') for _ in range(int(input()))]
print(snake(d))

