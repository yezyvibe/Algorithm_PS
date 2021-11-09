def solution(n):
    answer = 0
    while n:
        if n % 2 == 1:
            n -= 1
            answer += 1
        else:
            n = n//2
    return answer        