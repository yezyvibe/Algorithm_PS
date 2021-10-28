def solution(s):
    s = s[1:-1]
    s_lst = []
    tmp_str = ''
    tmp_lst = []
    for i in s:
        if i.isdigit():
            tmp_str += i
        elif i == ',' and tmp_str:
            tmp_lst.append(int(tmp_str))
            tmp_str = ''
        elif i == '}':
            if tmp_str != '':
                tmp_lst.append(int(tmp_str))
                tmp_str = ''
            s_lst.append(tmp_lst)
            tmp_lst = []

    if len(s_lst) == 1:
        return s_lst[0]
    s_lst.sort(key=lambda x:len(x))
    s_lst = [sorted(i, key=lambda x:x) for i in s_lst ]
    
    answer = [s_lst[0][0]]
    for i in range(1, len(s_lst)):
        for j in s_lst[i]:
            if j not in answer:
                answer.append(j)
    return answer


# def solution(s):

#     s = Counter(re.findall('\d+', s))
#     return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

# import re
# from collections import Counter


# def solution(s):
#     answer = []

#     s1 = s.lstrip('{').rstrip('}').split('},{')

#     new_s = []
#     for i in s1:
#         new_s.append(i.split(','))

#     new_s.sort(key = len)

#     for i in new_s:
#         for j in range(len(i)):
#             if int(i[j]) not in answer:
#                 answer.append(int(i[j]))

#     return answer