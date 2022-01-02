from collections import deque

s = int(input())
visit = [[0]*(s+1) for _ in range(s+1)] #행이 화면, 열이 클립보드
visit[1][0] = 1
q = deque([[1, 0]])

while q:
    x, y = q.popleft()
    # 1번 연산: 화면 -> 클립보드 저장 
    if not visit[x][x]:
        visit[x][x] = visit[x][y] + 1
        q.append([x, x])
    # 2번 연산: 클립보드 -> 화면 저장
    if x + y <=s and not visit[x+y][y]: 
        visit[x+y][y] = visit[x][y] + 1
        q.append([x+y, y])
    # 3번 연산: 화면에 있는 이모티콘 하나 삭제
    if x - 1 >= 0 and not visit[x-1][y]:
        visit[x-1][y] = visit[x][y] + 1
        q.append([x-1, y])


min_v = 1000000
for i in range(s+1):
    if visit[s][i]:
        min_v = min(min_v, visit[s][i])
print(min_v-1)