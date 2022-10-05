# 최단거리 -> bfs

from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[5]*(102) for i in range(102)]
    # 테두리와 내부 표시하기
    for i in range(len(rectangle)):
        a, b, c, d = map(lambda x:x*2, rectangle[i])
        # print(a, b, c, d)
        for j in range(a, c+1):
            for k in range(b, d+1):
                if a < j < c and b < k < d:
                    board[j][k] = 0 # 내부
                elif board[j][k] != 0: 
                    board[j][k] = 1

    queue = deque([(characterX*2, characterY*2)])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visit = [[0]*(102) for _ in range(102)]
    visit[characterX*2][characterY*2] = 1

    while queue:
        x, y = queue.popleft()
        if x == itemX * 2 and y == itemY * 2:
            return visit[x][y] // 2
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < 102 and 0 <= ny < 102:
                if not visit[nx][ny] and board[nx][ny] == 1:
                    queue.append((nx, ny))
                    visit[nx][ny] = visit[x][y] + 1


print(solution(	[[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))