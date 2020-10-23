import sys


def chess(a, b, c):
    cnt = 0
    for i in range(a, a + 8):
        for j in range(b, b + 8):
            if i == a and j == b:
                if c == 'W':
                    chk = 'B'
                    if bg[i][j] != c:
                        cnt += 1
                else:
                    chk = 'W'
                    if bg[i][j] != c:
                        cnt += 1
                continue

            if chk == 'W':
                if bg[i][j] != 'W':
                    cnt += 1
                chk = 'B'
            else:
                if bg[i][j] != 'B':
                    cnt += 1
                chk = 'W'

        if chk == 'W':
            chk = 'B'
        else:
            chk = 'W'
    return cnt


input = sys.stdin.readline
n, m = map(int, input().rstrip().split(' '))
bg = [list(input().rstrip()) for _ in range(n)]
min_v = 100000

for a in range(n - 7):
    for b in range(m - 7):
        cnt = chess(a, b, 'W')
        if cnt < min_v:
            min_v = cnt
        cnt = chess(a, b, 'B')
        if cnt < min_v:
            min_v = cnt

print(min_v)
