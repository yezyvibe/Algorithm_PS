import sys


input = sys.stdin.readline
h, w = map(int, input().split(' '))
area = [[-1]*w for _ in range(h)]
for i in range(h):
    a = list(input().rstrip())
    for j in range(len(a)):
        if a[j] == 'c':
            area[i][j] = 0
            cnt = 1
            j += 1
            while j < w:
                area[i][j] = cnt 
                cnt += 1
                j += 1
for i in area:
    print(' '.join(map(str, i)))