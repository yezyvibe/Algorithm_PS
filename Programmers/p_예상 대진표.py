def solution(n, a, b):
    answer = 0

    while a != b:
        answer += 1
        r_a, r_b = round(a / 2), round(b / 2)
        if r_a < (a / 2): # 반올림한 자리의 앞자리가 짝수인 경우
            a = r_a + 1
        else:
            a = r_a
        if r_b < (b / 2): # 반올림한 자리의 앞자리가 짝수인 경우
            b = r_b + 1
        else:
            b = r_b
    return answer