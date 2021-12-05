import sys


input = sys.stdin.readline
n = int(input())
paper = [[0]*101 for _ in range(101)]

for i in range(n):
    x, y = map(int, input().split())
    for j in range(x, x+10):
        for k in range(y, y+10):
            paper[j][k] = 1

answer = 0
for i in range(101):
    for j in range(101):
        if paper[i][j] == 1:
            answer += 1
print(answer)
