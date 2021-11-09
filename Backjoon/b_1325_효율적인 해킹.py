import sys
from collections import deque

input = sys.stdin.readline


def bfs(lst):
    q = deque(lst)
    while q:
        x = q.popleft()
        visit[x] = 1
        for i in adj[x]:
            if not visit[i]:
                q.append(i)
                visit[i] = 1
    return visit.count(1)


n, m = map(int, input().split(' '))
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split(' '))
    adj[b].append(a)

res = []
max_v = 0
for i in range(1, n + 1):
    visit = [0] * (n + 1)
    visit[i] = 1
    if adj[i]:
        tmp = bfs(adj[i])
        if tmp > max_v:
            max_v = tmp
            res = [i]
        elif tmp == max_v:
            res.append(i)

print(*res)
