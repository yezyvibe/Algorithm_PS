# 이분탐색 
def solution(n, cores):
    cores_len = len(cores)
    if n <= cores_len : return n

    n -= cores_len
    left, right = 1, max(cores)*n

    while left < right:
        mid = (left + right) // 2
        cnt = 0

        for core in cores:
            cnt += (mid // core)
        if cnt >= n:
            right = mid
        else:
            left = mid + 1
    
    for core in cores:
        n -= (right - 1) // core
    
    for i in range(cores_len):
        if right % cores[i] == 0:
            n -= 1
            if n == 0: return i + 1