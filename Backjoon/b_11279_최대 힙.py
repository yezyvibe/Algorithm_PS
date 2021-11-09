import sys, heapq

input = sys.stdin.readline

heap = []
for i in range(int(input())):
    t = int(input())

    if t == 0:
        if len(heap) == 0:
            res = 0
        else:
            res = heapq.heappop(heap)[1]
        print(res)

    else:
        heapq.heappush(heap, (-t, t))
