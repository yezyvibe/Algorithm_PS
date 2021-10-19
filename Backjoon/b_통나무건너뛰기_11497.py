from collections import deque
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    log_list = list(map(int, input().split()))
    log_list.sort()
    q = deque()
    for i in range(n):
        if i % 2 == 0:
            q.append(log_list[i])
        else:
            q.appendleft(log_list[i])
    max_v = -1
    for i in range(1, n):
        max_v = max(max_v, abs(q[i] - q[i-1]))
    print(max_v)