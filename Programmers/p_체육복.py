def solution(n, lost, reserve):
    students = [1] * (n + 1)
    students[0] = 0
    tmp = []

    for i in lost:
        students[i] = 0
        if i in reserve:
            students[i] = 1
            tmp.append(i)

    for i in tmp:
        lost.remove(i)
        reserve.remove(i)

    for i in reserve:
        if i - 1 == 0:
            if students[i + 1] == 0:
                students[i + 1] = 1
            continue
        if i + 1 == n + 1:
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