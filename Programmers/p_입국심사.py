def solution(n, times):
    # 이분탐색의 범위는 입국심사에 소요되는 총 시간
    # 기준은 mid 시간 동안 심사할 사람의 수
    times.sort()
    start, end = 1, times[-1] * n
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        people = 0
        for time in times:
            people += mid // time 
        if people >= n:
            end = mid - 1
            answer = mid
        else:
            start = mid + 1
    return answer
print(solution(6, [7, 10])) 