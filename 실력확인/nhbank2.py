def solution(birthdays):
    dic = {
        1:31, 3:31, 5:31, 7:31, 8:31, 10:31, 12:31,
        2:28,
        4:30, 6:30, 9:30, 11:30,
    }
    birthdays.sort()
    weekend = []
    for i in range(len(birthdays)):
        cur = birthdays[i]
        m, d = cur[:2], cur[2:]
        total = int(d)
        for j in range(1, int(m)):
            total += dic[j]
        r = total % 7
        if r == 0 or r == 1: # 토요일 또는 일요일 아예 못 받는다
            weekend.append(cur)

    # 생일 선물 개수 세기
    answer = 0
    for i in range(len(birthdays)):
        cur = birthdays[i]
        if cur in weekend: # 주말이니까 선물 못 받는다 패스
            continue
        cur_day = int(cur[2:])
        for j in range(1, int(cur[:2])):
            cur_day += dic[j]
        cnt = 0 # 5일 미만이라 못 받는 횟수
        for j in range(len(birthdays)):
            if i == j:
                continue
            next = birthdays[j]
            next_day = int(next[2:])
            for j in range(1, int(next[:2])):
                next_day += dic[j]
            if abs(next_day - cur_day) < 5:
                cnt += 1
        res =  len(birthdays) - 1 - cnt
        if res > 0:
            answer += res
    return answer