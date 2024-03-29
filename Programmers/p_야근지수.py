import heapq

def solution(n, works):
    answer = 0
    if sum(works) <= n:
        return 0

    hq = []
    for i in works:
        heapq.heappush(hq, -i)

    while n:
        max_work = heapq.heappop(hq) + 1
        n -= 1
        heapq.heappush(hq, max_work)

    return sum([i**2 for i in hq])

print(solution(3, [1, 1]))