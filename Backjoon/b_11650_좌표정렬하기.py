import sys

input = sys.stdin.readline
num = []
for i in range(int(input())):
    x, y = map(int, input().split())
    num.append((x, y))
num.sort()
# num.sort(key=lambda x: (x[0],x[1]))
for a, b in num:
    print(a,b)