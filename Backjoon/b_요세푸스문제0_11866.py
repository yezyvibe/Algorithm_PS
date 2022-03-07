import sys
from collections import deque


input = sys.stdin.readline
n, k = map(int, input().split())
q = deque([i for i in range(1, n+1)])
index = 0
answer = []

while q:
    tmp = q.popleft()
    index += 1
    if index == k:
        answer.append(str(tmp))
        index = 0
    else:
        q.append(tmp)
answer[0] = '<'+ answer[0]
answer[-1] = answer[-1] + '>'
print(', '.join(answer))
    

