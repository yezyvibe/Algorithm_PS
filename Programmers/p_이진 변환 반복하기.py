def solution(s):
    change_cnt = 0
    cnt_0 = 0
    while s != '1':
        change_cnt += 1
        cnt_0 += s.count('0')
        cnt_1 = len(s)-(s.count('0'))
        s = bin(cnt_1)[2:]
    return [change_cnt, cnt_0]