import sys
import heapq
input = sys.stdin.readline
n, k = map(int, input().split())
jewelry = []
for i in range(n):
    weight, price = map(int, input().rstrip().split())
    heapq.heappush(jewelry, [weight, price])
bags = [int(input()) for _ in range(k)]
bags.sort()   # 가벼운 것부터 무거운 순으로 정렬

answer = 0
tmp = []
for bag in bags:
    while jewelry and bag >= jewelry[0][0]:   # 가방에 담을 수 있는 최대 무게보다 가벼운 보석들을 모두 담기
        heapq.heappush(tmp, -heapq.heappop(jewelry)[1])
    if tmp:
        answer -= heapq.heappop(tmp)
    elif not jewelry:
        break
print(answer)    