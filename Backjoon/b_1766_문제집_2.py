import sys
import heapq



input = sys.stdin.readline
n, m = map(int, input().split())
degree = [ [0, []] for _ in range(n+1)]
solved = [0] * (n+1)
hq = []
answer = []

for _ in range(m):
    a, b = map(int, input().split())
    degree[b][0] += 1 # b를 풀기 전 a를 먼저 풀기
    degree[a][1].append(b)

for i in range(1, n+1):
    if degree[i][0] == 0:
        # 먼저 풀기
        heapq.heappush(hq, i)
        
while hq:
    cur = heapq.heappop(hq)
    answer.append(cur)

    # 차수 내리기
    for k in degree[cur][1]:
        degree[k][0] -= 1
        if degree[k][0] == 0:
            heapq.heappush(hq, k)

print(*answer)
