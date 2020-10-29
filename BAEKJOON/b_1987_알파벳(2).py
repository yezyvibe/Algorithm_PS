import sys

# 좌, 하, 우, 상
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def BFS(x, y):
    global answer
    q = set([(x, y, board[x][y])])

    while q:
        x, y, ans = q.pop()

        # 좌우상하 갈 수 있는지 살펴본다
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # index 벗어나지 않는지 체크하고, 새로운 칸이 중복되는 알파벳인지 체크한다
            if ((0 <= nx < R) and (0 <= ny < C)) and (board[nx][ny] not in ans):
                q.add((nx,ny,ans + board[nx][ny]))
                answer = max(answer, len(ans)+1)


R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]

answer = 1
BFS(0, 0)
print(answer)


# import sys
#
#
# def dfs(x, y, alpha):
#     global answer
#     cnt = 0
#     for k in range(4):
#         nx, ny = x + dx[k], y + dy[k]
#         if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in alpha:
#             dfs(nx, ny, alpha+board[nx][ny])
#         else:
#             cnt += 1
#     if cnt == 4:
#         answer = max(answer, len(alpha))
#         return
#
#
# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
# input = sys.stdin.readline
# r, c = map(int, input().split(' '))
# board = [list(input().rstrip()) for _ in range(r)]
# answer = 1
# dfs(0, 0, board[0][0])
# print(answer)
