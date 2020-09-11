import heapq
def solution(scoville, K):
    items = []
    for i in scoville:
        heapq.heappush(items, i)
    cnt = 0
    while items[0] < K:
        try:
            heapq.heappush(items, heapq.heappop(items)+(heapq.heappop(items)*2))
        except:
            return -1
        cnt += 1
    return cnt