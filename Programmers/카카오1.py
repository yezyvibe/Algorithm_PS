def solution(new_id):
    answer = ''
    chk = ['-', '_', '.']
    for i in new_id:
        if i.isalpha():
            i = i.lower()
            answer += i
        elif i.isdigit() or i in chk:
            answer += i

    cnt = 0
    tmp = ''
    for i in answer:
        if i == '.':
            cnt += 1
        else:
            if cnt != 0:
                tmp += '.'
                cnt = 0
            tmp += i

    tmp = tmp.strip('.')

    if not tmp:
        tmp = 'a'

    if len(tmp) >= 16:
        tmp = tmp[0:15]
        if tmp[-1] == '.':
            tmp = tmp[0:14]
    if len(tmp) <= 2:
        last_c = tmp[-1]
        while len(tmp) != 3:
            tmp += last_c

    return tmp










