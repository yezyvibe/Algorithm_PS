import sys


def dfs(i, j, h):
    s = [(i, j)]
    while s:
        x, y = s.pop()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if visit[nx][ny] == 0 and bg[nx][ny] > h:
                    visit[nx][ny] = 1
                    s.append((nx, ny))

input = sys.stdin.readline
n = int(input())
bg = [list(map(int, input().rstrip().split(' '))) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
res = 0

for h in range(max(map(max, bg))):
    visit = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if bg[i][j] > h and visit[i][j] == 0:
                cnt += 1
                visit[i][j] = 1
                dfs(i, j, h)

    res = max(res, cnt)
print(res)

# 효율적인 풀이
# def fill(board, row, col) :
#     board[row][col] = False
#     n = len(board)
#     directs = [[0,1],[1,0],[0,-1],[-1,0]]
#     for direct in directs :
#         drow, dcol = row+direct[0], col+direct[1]
#         if 0 <= drow < n and 0 <= dcol < n :
#             if board[drow][dcol] == True :
#                 fill(board, drow, dcol)
#
# if __name__ == '__main__' :
#     n = int(input())
#     board = []
#     min_val, max_val = 0, 101
#     for _ in range(n) :
#         row = list(map(int, input().split()))
#         board.append(row)
#         min_val, max_val = min(min_val,min(row)), max(max_val,max(row))
#     res = 1
#     for depth in range(min_val, max_val+1) :
#         remain_board = []
#         for row in board :
#             remain_board.append(list(map(lambda x : x > depth, row)))
#         temp = 0
#         try :
#             for row in range(n) :
#                 for col in range(n) :
#                     if remain_board[row][col] == True :
#                         fill(remain_board, row, col)
#                         temp += 1
#             res = max(res, temp)
#         except :
#             pass
# print(res)