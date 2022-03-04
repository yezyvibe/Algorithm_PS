from collections import deque


n, k = map(int, input().split())
dirs = [-1, 1, 2]
q = deque([[n, 0]])
visit = [0]*100001
path = [0]*100001
visit[n] = 1

while q:
    current, cnt = q.popleft()
    if current == k:
        print(cnt)
        answer = []
        while current != n:
            answer.append(current)
            current = path[current]
        answer.append(n)
        answer.reverse()
        print(' '.join((map(str, answer))))
        break
    for i in range(3):
        if i == 2:
            next = current*2
        else:
            next = current + dirs[i]
    
        if 0 <= next <= 100000 and not visit[next]:
            q.append([next, cnt + 1])
            visit[next] = 1
            path[next] = current