import sys

input = sys.stdin.readline
n, m = map(int, input().rstrip().split(' '))
ball_list = [i for i in range(1, n+1)]

for k in range(m):
    i, j = map(int, input().rstrip().split(' '))
    ball_list[i-1], ball_list[j-1] = ball_list[j-1], ball_list[i-1]
print(' '.join(map(str, ball_list)))