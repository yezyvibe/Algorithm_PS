def solution(dartResult):
    answer = 0
    res = {}
    idx = -1
    check = 1

    # 기회별 점수 -> 딕셔너리에 구분해 넣기
    for i in dartResult:
        if i.isdigit():
            if check == 1:
                idx += 1
                res[idx] = ''
                res[idx] += i
            elif check == 0: # 10처리
                res[idx] = '_'
            check = 0
        else:
            res[idx] += i
            check = 1

    for key, value in res.items():
        tmp = 0
        for i in value:
            # 점수
            if i.isdigit():
                tmp = int(i)
            # 10 처리
            elif i == '_':
                tmp = 10

            # 보너스
            elif i == 'S':
                tmp = tmp ** 1
            elif i == 'D':
                tmp = tmp ** 2
            elif i == 'T':
                tmp = tmp ** 3

            # 옵션
            if i == '*':
                tmp = tmp * 2
                res[key] = tmp
                if key != 0:
                    res[key - 1] = res[key - 1] * 2
                    break
                break
            elif i == '#':
                res[key] = -tmp
                break
            res[key] = tmp
    # 합산
    for i in res.values():
        answer += i
    return answer