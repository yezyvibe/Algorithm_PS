def solution(n):
    answer = 1
    for i in range(1, n//2+1):
        tmp = 0
        for j in range(i, n//2+2):
            tmp += j
            if tmp > n:
                break
            if tmp == n:
                answer += 1
                break
    return answer