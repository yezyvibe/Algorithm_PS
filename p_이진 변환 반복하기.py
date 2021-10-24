def solution(s):
    result = [0, 0]
    cnt = 0
    zero_cnt = 0
    while s != '1':
        cnt += 1
        tmp = ''
        for i in s:
            if i == '1':
                tmp += i
            else:
                zero_cnt += 1
        s = len(tmp)
        s = bin(s)[2:]
    result[0] = cnt
    result[1] = zero_cnt
    return result
    

print(solution("110010101001"))