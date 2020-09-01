def solution(n, lost, reserve):
    students = [1] * (n + 1)
    students[0] = 0
    tmp = []

    for i in lost:
        students[i] = 0
        if i in reserve:
            students[i] = 1
            tmp.append(i)

    for i in tmp: # 여분 가지고 있는 학생이 체육복을 잃어 버린 경우
        lost.remove(i)
        reserve.remove(i)

    for i in reserve:
        if i - 1 == 0: # 인덱스 1인 경우에는 2번째만 체크
            if students[i + 1] == 0:
                students[i + 1] = 1
            continue
        if i + 1 == n + 1: # 인덱스 n인 경우(끝값) n-1번째만 체크
            if students[i - 1] == 0:
                students[i - 1] = 1
            continue
        if students[i - 1] == 0:
            students[i - 1] = 1
            continue
        if students[i + 1] == 0:
            students[i + 1] = 1
            continue

    return sum(students)