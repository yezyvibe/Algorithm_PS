import heapq

def solution(jobs):
    n = len(jobs)
    start, end = 0, 0
    heap = []
    jobs.sort(key=lambda x : -x[0])
    answer = 0 
    while jobs or heap:
        while jobs and start <= jobs[-1][0] <= end:
                point, time = jobs.pop()
                heapq.heappush(heap, [time, point])
        if heap:
            time, point = heapq.heappop(heap)    
            start = end
            end += time
            answer += (end-point)
        else:
            end += 1
    return answer // n


jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))