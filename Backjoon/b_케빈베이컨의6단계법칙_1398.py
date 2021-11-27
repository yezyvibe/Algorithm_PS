# 블로그 정리하기 -> 처음 dfs로 풀어서 오류 
# -> bfs로 수정 (출발지에서 각 노드까지의 최단거리를 찾는 개념이기 때문에)


import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)


min_v = 1000000000
answer = 0
for i in range(1, n+1):
    visit = [0]*(n+1)
    q = deque([(i, 0)])
    visit[i] = 1
    while q:
        x, cnt = q.popleft()
        for k in adj[x]:
            if not visit[k]:
                q.append((k, cnt + 1))
                visit[k] = cnt + 1

    tmp = sum(visit)
    if min_v > tmp:
        answer = i
        min_v = tmp
print(answer)

    