def get_divisor(n):
    res = []
    for i in range(1, n+1):
        if n % i == 0:
            res.append(i)
    return res

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        divisor = get_divisor(i)
        if len(divisor) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer