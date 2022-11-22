# import sys
# from heapq import heappop, heappush


# input = sys.stdin.readline
# N = int(input())
# degrees = [0] * (N+1)
# times = [0] * (N+1)
# graph = [[] for _ in range(N+1)]

# for current in range(1, N + 1):
#     time, count, *nodes = map(int, input().split())

#     times[current] = time
#     degrees[current] = count

#     for node in nodes:
#         graph[node].append(current)

# heap = []

# for node in range(1, N+1):
#     if degrees[node] == 0:
#         heappush(heap, (times[node], node))

# while heap:
#     end_time, current = heappop(heap)

#     for node in graph[current]:
#         degrees[node] -= 1

#         if degrees[node] == 0:
#             heappush(heap, (end_time + times[node], node))


# print(end_time)



import sys
import heapq

input = sys.stdin.readline

n = int(input())
degree = [0] * (n+1)
before_works = [[0, []] for _ in range(n+1)]
visit = [0] * (n+1)

for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    time, cnt, arr = tmp[0], tmp[1], tmp[2:]
    before_works[i][0] = time
    for j in arr:
        before_works[j][1].append(i)
    degree[i] = cnt

hq = []
for i in range(1, n+1):
    if degree[i] == 0:
        heapq.heappush(hq, (before_works[i][0], i))

while hq:
    end_time, cur_work = heapq.heappop(hq)

    # 차수 빼고 확인
    for k in before_works[cur_work][1]:
        degree[k] -= 1
        least_time = before_works[k][0]

        if degree[k] == 0 and not visit[k]:
            visit[k] = 1
            heapq.heappush(hq, (end_time + least_time, k))

print(end_time)