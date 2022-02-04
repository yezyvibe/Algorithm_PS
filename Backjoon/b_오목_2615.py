import sys


input = sys.stdin.readline
omok = [list(map(int, input().split())) for _ in range(19)]
dx, dy = [-1, 0, 1, 1], [1, 1, 1, 0]   # 우상, 우, 우하, 하 4가지 방향 탐색

def check_boundary(x, y):
    if 0 <= x < 19 and 0 <= y < 19:
        return True
    return False

def search(x, y, color):
    for k in range(4):
        bx, by = x - dx[k], y - dy[k]
        # 반대방향으로 돌이 있는지, 색이 같은지 체크
        if not check_boundary(bx, by) or omok[bx][by] != color:   # 경계를 넘어가는 경우나 같은 색이 아닌 경우에만 탐색 이어서
            nx, ny = x + dx[k], y + dy[k]
            cnt = 1
            while True:
                # 경계 체크, 같은 색상의 돌인지 확인
                if check_boundary(nx, ny) and omok[nx][ny] == color:
                    cnt += 1
                else:
                    break
                # 조건을 충족하면 계속 이동
                nx += dx[k]
                ny += dy[k]
            if cnt == 5:
                return True
    else:
        return False

def main():
    for i in range(19):
        for j in range(19):
            if omok[i][j] != 0:  # 오목 시작점
                if search(i, j, omok[i][j]):
                    return [omok[i][j], i+1, j+1]
    return [0, 0, 0]

winner, x, y = main()
if winner == 0:
    print(0)
else:
    print(winner)
    print(x, y)
