def solution(n, s):
    if n > s:
        return [-1]

    quotient = s // n
    result = [quotient] * n
    if s % n != 0:
        remainder = s % n
        idx = -1
        for i in range(remainder):
            result[idx] += 1
            idx -= 1
    return result



solution(2, 1)