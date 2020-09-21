def solution(s):
    answer = ''
    chk = 1
    for i in s:
        if i == ' ':
            answer += i
            chk = 1
        elif chk == 1:
            i = i.upper()
            answer += i
            chk = 0
        else:
            i = i.lower()
            answer += i
    return answer

# def solution(s):
#     answer = ''
#     chk = 0
#     s = s.lower()
#     s = [list(i) for i in s.split()]
#     for i in range(len(s)):
#         s[i][0] = s[i][0].upper()
#     for i in s:
#         i = ''.join(i)+' '
#         answer += i
#     return answer[:-1]

