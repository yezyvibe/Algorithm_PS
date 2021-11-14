import sys

input = sys.stdin.readline
n = int(input())
level = []
for i in range(n):
    level.append(int(input()))
answer = 0
for i in range(n-1, 0, -1):
    if level[i] <= level[i-1]:   #뒤의 것보다 앞의 거가 더 큰 경우
        answer += level[i-1] - level[i] + 1
        level[i-1] = level[i] - 1


print(answer, level)