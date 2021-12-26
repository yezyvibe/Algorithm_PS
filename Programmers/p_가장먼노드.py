from collections import deque


def solution(n, edge):

    adj = [[] for _ in range(n+1)]
    visit = [0] * (n+1)
    for a, b in edge:
        adj[a].append(b)
        adj[b].append(a)
    
    visit[1] = 1
    q = deque([1])
    
    while q:
        x = q.popleft()
        for next in adj[x]:
            if not visit[next]:
                visit[next] = visit[x] + 1
                q.append(next)
    
    max_v = max(visit)
    cnt = visit.count(max_v)

    return cnt if cnt > 0 else 1
    



print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]] ))