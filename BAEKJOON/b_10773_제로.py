import sys

input = sys.stdin.readline

num = []
for i in range(int(input())):
    n = int(input())
    if n != 0:
        num.append(n)
    else:
        num.pop()
print(sum(num))
