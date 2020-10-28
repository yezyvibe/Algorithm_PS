import heapq


def solution(jobs):
    candidates = []
    f = -1  # 구간 시작
    t = 0  # 구간 끝
    res = 0  # 결과값
    cnt = 0  # 결과개수
    while cnt < len(jobs):
        for job in jobs:
            if f < job[0] <= t:
                res += (t - job[0])  #대시 시간
                print(t-job[0], '대기시간')
                heapq.heappush(candidates, job[1])

        if len(candidates) > 0:
            res += (len(candidates) * candidates[0])
            f = t
            t += heapq.heappop(candidates)
            cnt += 1
        else:
            t += 1
    return res // len(jobs)


# jobs = [[0, 20], [3, 4], [3, 5], [17,2]]
jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))
