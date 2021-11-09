import sys

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visit = [0] * n

for k in range(n):
    for i in range(n):
        for j in range(n):
            if (arr[i][j] == 1) or (arr[i][k] == 1 and arr[k][j] == 1):
                arr[i][j] = 1

for a in arr:
    print(' '.join(map(str, a)))


# def bfs(i, arr, n):
#     visit = [0]*n
#     queue = [i]
#
#     while queue:
#         index = queue.pop(0)
#         for idx, val in enumerate(arr[index]):
#             if visit[idx] == 0 and val == 1:
#                 visit[idx] = 1
#                 queue.append(idx)
#     return visit
#
#
# n = int(sys.stdin.readline())
# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# visit = [0] * n
#
# for i in range(n):
#     print(' '.join(map(str, bfs(i, arr, n))))
