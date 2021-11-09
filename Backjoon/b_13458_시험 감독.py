import sys
import math
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().rstrip().split(' ')))
b, c = map(int, input().rstrip().split(' '))

cnt = 0
for a in arr:
    tmp = a - b
    cnt += 1
    if tmp <= 0:
        continue
    cnt += math.ceil(tmp / c)
print(cnt)