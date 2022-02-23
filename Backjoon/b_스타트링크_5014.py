from collections import deque


f, s, g, u, d = map(int, input().split())
visit = [0]*(f+1)
q = deque([[s, 0]])
visit[s] = 1
dirs = [u, -d]
while q:
    current, cnt = q.popleft()
    if current == g:
        print(cnt)
        break
    for k in dirs:
        next = current + k
        if 1 <= next <= f and not visit[next]:
            q.append([next, cnt + 1])
            visit[next] = 1
else:
    print('use the stairs')