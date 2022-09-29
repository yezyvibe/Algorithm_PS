import sys

# 최소 간선 개수

def dfs(start, n):
    s = [start]
    visit = [0] * (n+1)
    while s:
        cur = s.pop()
        for i in adj[cur]:
            if not visit[i]:
                visit[i] = 1
                s.append(i)
    return sum(visit) == n

input = sys.stdin.readline
for tc in range(int(input())):
    n, m = map(int, input().split(" "))
    adj = [[] for _ in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split(" "))
        adj[a].append(b)
        adj[b].append(a)
    if dfs(1, n):
        print(n-1)
    



