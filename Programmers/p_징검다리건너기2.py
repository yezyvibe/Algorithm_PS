def solution(stones, k):
    start = 1
    end = 200000000
    mid = (start + end) // 2

    while start <= end:
        cnt = 0
        mid = (start + end) // 2
        for stone in stones:
            if (stone - mid) <= 0:
                cnt += 1
                if cnt >= k:
                    end = mid - 1
                    break
            else:
                cnt = 0
        else:
            start = mid + 1
    return start
            
            
stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones, k))