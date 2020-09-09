def solution(s, n):
    answer = ''
    s = list(s)
    for a in s:
        if a != ' ':
            num = ord(a) + n
            if 65 <= ord(a) <= 90: # 대문자
                if num > 90:  # 마지막 Z를 넘어가는 경우 처리
                    num = num - 26
                res = chr(num)
            else:                  # 소문자
                if num > 122: # 마지막 z 넘가는 경우
                    num = num - 26
                res = chr(num)
            answer += res
        else: # 공백 문자 처리
            answer += a
    return answer