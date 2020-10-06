import sys
import heapq

input = sys.stdin.readline
heap = []
for i in range(int(input())):
    t = int(input())
    if t == 0:
        if len(heap) == 0:
            res = 0
            print(res)
        else:
            res = heapq.heappop(heap)
            print(res)
    else:
        heapq.heappush(heap, t)