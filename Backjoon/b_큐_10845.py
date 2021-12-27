import sys
from collections import deque


input = sys.stdin.readline
q = deque()
for i in range(int(input())):
    order = input().rstrip()
    if order[0:2] == 'pu':
        order = order.split(' ')
        q.append(order[1])
    elif order == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif order == 'size':
        print(len(q))
    elif order == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif order == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif order == 'back':
        print(q[-1]) if q else print(-1)
    