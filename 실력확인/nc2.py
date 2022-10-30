from collections import deque

def bfs(s, e, adj):
    q = deque([(s, 0)])    
    visit = [0] * (13)
    visit[s] = 1
    while q:
        x, cnt = q.popleft()
        if x == e:
            return cnt
        for k in adj[x]:
            if not visit[k]:
                q.append((k, cnt + 1))
                visit[k] = 1


# 피아노 건반 최소로 이동해서 누르기

def solution(music):
    adj = [[], [2, 3], [1, 3], [1, 2, 4, 5], [3, 5], [3, 4, 6, 7],  #12345
    [5, 7], [5, 6, 8], [7, 9, 10], [8, 10], [8, 9, 11, 12], [10, 12], [10, 11]] # 6789101112

    # 1부터 시작
    answer = 0
    for i in range(len(music)):
        if i == 0:
            answer = bfs(1, music[i], adj)
            continue
        answer += bfs(music[i-1], music[i], adj)
    return answer