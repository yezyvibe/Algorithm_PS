def solution(n, times):
    # 이분 탐색의 범위 -> 검사하는데 걸리는 총 시간
    # 이분 탐색의 기준 -> mid 시간 동안 검사 받은 사람의 수
    times.sort()
    start, end = 1, times[-1] * n
    answer = 0
    while start <= end:
        mid = (start + end) // 2            
        completed = 0
        for cur_inspector in times:
            completed += (mid // cur_inspector) # mid 시간 동안 각 검사관이 검사할 수 있는 사람의 수 더하기
            if completed >= n:
                break
        if completed >= n:
            end = mid - 1
            answer = mid
        else:
            start = mid + 1
    return answer

print(solution(6, [7,10]))
