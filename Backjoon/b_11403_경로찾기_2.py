import sys
from collections import deque

def bfs(s):
    q = deque([s])
    visit = [0] * n

    while q:
        cur_node = q.popleft()

        for k in range(n):
            if arr[cur_node][k] and not visit[k]:
                visit[k] = 1
                q.append(k)
    return visit

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    print(" ".join(map(str, bfs(i))))
            
