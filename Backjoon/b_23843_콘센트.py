import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
electronics = list(map(int, input().split()))
electronics.sort()
heap = []

for i in range(n-1, -1, -1):
    cur = electronics[i]

    if len(heap) < m:
        heapq.heappush(heap, cur)
    else:
        min_v = heapq.heappop(heap)
        heapq.heappush(heap, cur+min_v)

print(max(heap))