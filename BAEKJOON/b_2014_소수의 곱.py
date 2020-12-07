import sys
import heapq

input = sys.stdin.readline

k, n = map(int, input().split(' '))
arr = list(map(int, input().rstrip().split(' ')))
heap = []
for i in range(len(arr)):
    heapq.heappush(heap, arr[i])
# print(heap)
for _ in range(n):
    num = heapq.heappop(heap)
    # print(i, 'num시작:', num)
    for i in range(len(arr)):
        tmp = arr[i] * num
        heapq.heappush(heap, tmp)
        # print('우선순위큐:', heap)
        if num % arr[i] == 0:
            break
print(num)
