from collections import deque


a, b = map(int, input().split())
q = deque([(a, 0)])
while q:
    x, cnt = q.popleft()
    if x == b:
        print(cnt+1)
        break
    for i in range(2):
        if i == 0:
            tmp = x  * 2
        else:
            tmp = int(str(x)+'1')
        if tmp <= b:
            q.append((tmp, cnt + 1))
else:
    print(-1)