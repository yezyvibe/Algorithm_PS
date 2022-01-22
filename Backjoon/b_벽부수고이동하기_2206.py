import sys
from collections import deque

def bfs():
    visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque([(0, 0, 1)])
    visit[0][0][1] = 1  # arr[x][y] 방문했다고 표시
    while q:
        a, b, w = q.popleft()
        if a == n - 1 and b == m - 1:
            return visit[a][b][w]
        for k in range(4):
            na, nb = a + dx[k], b + dy[k]
            if 0 <= na < n and 0 <= nb < m:
                if arr[na][nb] == '0' and not visit[na][nb][w]:   # 방문한 적이 없는데 벽이 아닌 갈 수 있는 길이다
                    visit[na][nb][w] = visit[a][b][w] + 1 # 방문 길이 + 1
                    q.append((na, nb, w))  # 이전에 벽 뚫었는지 상태 그대로 저장
                elif arr[na][nb] == '1' and w == 1:  # 벽이라 갈 수 없는데, 벽을 뚫을 수 있는 기회가 남아 있다면
                    visit[na][nb][0] = visit[a][b][w] + 1
                    q.append((na, nb, 0)) # 더 이상 벽을 뚫을 수 없는 상태로 저장
                    
    return -1
    
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]

answer = bfs()
print(answer if answer > 0 else -1)