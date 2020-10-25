import sys

input = sys.stdin.readline
n = int(input())
cnt = [0]*10001
for i in range(n):
    number = int(input())
    cnt[number] += 1

for i in range(len(cnt)):
    if cnt[i] != 0:
        for k in range(cnt[i]):
            print(i)

