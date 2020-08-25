def solution(s):
    answer = []
    a = s.split(',{')
    a.sort(key = len)
    tmp = ''
    for i in a:
        for k in i:
            if k == ',':
                if int(tmp) not in answer:
                    answer.append(int(tmp))
                tmp = ''
            elif k !='{' and k != '}':
                tmp += k
        else:
            if int(tmp) not in answer:
                answer.append(int(tmp))
            tmp = ''
    return answer