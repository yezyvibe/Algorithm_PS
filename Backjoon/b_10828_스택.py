import sys

input = sys.stdin.readline
n = int(input())
s = []
for t in range(n):
    tmp = input().split()
    c = tmp[0]
    if c == 'push':
        s.append(tmp[1])
        continue
    elif c == 'pop':
        try:
            res = s.pop()
        except:
            res = -1
    elif c == 'size':
        res = len(s)
    elif c == 'empty':
        if len(s) == 0:
            res = 1
        else:
            res = 0
    elif c == 'top':
        if len(s) == 0:
            res = -1
        else:
            res = s[-1]
    print(res)
