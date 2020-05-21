def connect(v):
    global cnt
    stack = [v]
    visit[v] = 1
    while stack:
        tmp = stack.pop()
        for i in adj[tmp]:
            if visit[i] == 0:
                stack.append(i)
                visit[i] = 1
    if visit.count(1) != n:
        for k in range(1, len(visit)):
            if visit[k] == 0:
                cnt += 1
                connect(k)
    return

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
visit = [0]*(n+1)
cnt = 1
for i in range(m):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)
connect(1)
print(cnt)
