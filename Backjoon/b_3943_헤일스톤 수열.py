import sys

input = sys.stdin.readline
for i in range(int(input())):
    n = int(input())
    res = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        res.append(n)
    print(max(res))