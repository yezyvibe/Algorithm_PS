def solution(info, query):
    answer = []
    info = [i.split(' ') for i in info]
    q = [i.split(' ') for i in query]
    idx = 0
    chk = 0
    while idx < len(query):
        lang = q[idx][0]
        position = q[idx][2]
        jors = q[idx][4]
        food = q[idx][6]
        score = q[idx][7]
        q_lst = [lang, position, jors, food, score]
        cnt = 0
        for i in info:
            for k in range(4):
                if q_lst[k] == '-':
                    continue
                if i[k] == q_lst[k]:
                    continue
                else:
                    chk = 1
                    break
            else:
                if int(i[-1]) >= int(q_lst[4]):
                    cnt += 1
        else:
            answer.append(cnt)
            cnt = 0
        idx += 1

    return answer