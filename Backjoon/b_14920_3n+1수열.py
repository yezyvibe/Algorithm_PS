import sys


input = sys.stdin.readline
cnt = 1 
num = int(input())
while num != 1:
    if num % 2 == 0:
        num = num // 2
    else:
        num = 3*num + 1
    cnt += 1
print(cnt)

