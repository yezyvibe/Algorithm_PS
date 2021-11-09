from collections import deque

# 너비 우선 탐색
n, k = map(int, input().split(' '))
arr = [0] * (k + 1)
max_v = 100001
visit = [0] * max_v
q = deque([n])
da = [-1, 1, 2]

while q:
    a = q.popleft()
    if a == k:
        print(visit[a])
        break

    for i in range(3):
        if i == 2:
            na = a * da[i]
        else:
            na = a + da[i]
        # a가 기존, na는 다시 돌아왔을 때 비교
        if (0 <= na < max_v) and (visit[na] == 0 or visit[a] + 1 < visit[na]):
            visit[na] = visit[a] + 1  # 카운트 해줌(갱신)
            q.append(na)


# from collections import deque
#
# def solution():
#     S, D = map(int, input().split())
#     visited = [0 for _ in range(100001)]
#     queue = deque([S])
#
#     # bfs
#     while queue:
#         pos = queue.popleft()
#         if pos == D:
#             return visited[pos]
#         for i in [pos-1,pos+1,pos*2]:
#             if 0<= i <= 100000 and visited[i] == 0:
#                 visited[i] = visited[pos] + 1
#                 queue.append(i)
#
# print(solution())