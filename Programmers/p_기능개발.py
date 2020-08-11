def solution(progresses, speeds):
    cnt_lst = []
    for i in range(len(progresses)):
        tmp = (100 - progresses[i])
        if (tmp % speeds[i]):
            cnt = tmp // speeds[i] + 1
            cnt_lst.append(cnt)
        else:
            cnt = tmp // speeds[i]
            cnt_lst.append(cnt)
    max_v = -111111
    cnt = 0
    result = []
    for i in range(len(cnt_lst)):
        tmp = cnt_lst.pop(0)
        if tmp >= max_v:
            cnt += 1
            max_v = tmp
            if i != 0 and cnt == 1:
                result.append(1)
        else:
            cnt += 1
            result.append(cnt)
            cnt = 0
    return result