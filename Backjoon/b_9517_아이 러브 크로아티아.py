import sys

input = sys.stdin.readline
start = int(input())
time = 210

for i in range(int(input())):
    a, b = map(str, input().split())
    time -= int(a)
    if time <= 0:
        print(start)
        break
    if b == 'T':
        start += 1
        if start > 8:
            start = 1
# print(start)
