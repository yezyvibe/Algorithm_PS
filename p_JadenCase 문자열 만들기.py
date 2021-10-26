def solution(s):
    s = s.lower().split(' ')
    for i in range(len(s)):
        if s[i] == '':
            continue
        s[i] = s[i][0].upper() + s[i][1:]
    return ' '.join(s)

# s = "for   the  last week"
# print(solution(s))