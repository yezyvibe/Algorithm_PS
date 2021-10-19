import heapq

n, m = map(int, input().split())
card = list(map(int, input().split()))
card.sort()
for i in range(m):
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    for j in range(2):
        heapq.heappush(card, a+b)
print(sum(card))