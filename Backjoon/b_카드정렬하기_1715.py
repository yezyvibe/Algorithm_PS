import sys
import heapq
input = sys.stdin.readline
n = int(input())
heap = []
for i in range(n):
    heapq.heappush(heap, int(input()))
answer = 0
while n != 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    heapq.heappush(heap, a+b)
    answer += (a+b)
    n -= 1
print(answer)