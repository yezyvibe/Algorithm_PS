import sys


input = sys.stdin.readline
n, m = map(int, input().split())
ball_basket = [0]*n
for l in range(m):
    i, j, k = map(int, input().split())
    for num in range(i-1, j):
        ball_basket[num] = k
print(' '.join(map(str, ball_basket)))    