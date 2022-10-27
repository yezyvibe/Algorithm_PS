import heapq


def solution(n, works):
    if sum(works) < n:
        return 0

    hq = []
    for i in range(len(works)):
        heapq.heappush(hq, (-works[i], i))

    for i in range(n):
        work, idx = heapq.heappop(hq)
        if -work >= 1:
            works[idx] -= 1
            work += 1
        if work:
            heapq.heappush(hq, (work, idx))

    return sum([i**2 for i in works])


print(solution(	3, [1, 1]))