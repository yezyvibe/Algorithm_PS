def solution(n, s):
    answer = [-1]
    if n > s:
        return answer

    q, r = divmod(s, n)
    answer = [q] * n    
    for i in range(n-1, n-1-r, -1):
        answer[i] += 1

    return answer

print(solution(2, 9))