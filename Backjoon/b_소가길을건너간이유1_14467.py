import sys

input = sys.stdin.readline
n = int(input())
cows = [-1]*n
answer = 0
for _ in range(n):
    number, position = map(int, input().split())
    number -= 1
    if cows[number] == -1:
        cows[number] = position
        continue
    if cows[number] != position:
        answer += 1
        cows[number] = position
print(answer)
