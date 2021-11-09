import sys
from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    visit[v] = 1
    while q:
        tmp = q.popleft()
        for i in adj[tmp]:
            if visit[i] == 0:
                q.append(i)
                visit[i] = visit[tmp] + 1

input = sys.stdin.readline
n = int(input())
t_s,t_b = map(int, input().split())
m = int(input())
adj = [[] for _ in range(n+1)]
visit = [0]*(n+1)
for i in range(m):
    p, c = map(int, input().split())
    adj[p].append(c)
    adj[c].append(p)
bfs(t_s)

print(visit[t_b]-1 if visit[t_b] else -1)