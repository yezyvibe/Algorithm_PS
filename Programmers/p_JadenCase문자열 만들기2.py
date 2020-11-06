def solution(s):
    s = s.split(' ')

    for i in range(len(s)):
        if s[i] != '':
            s[i] = s[i].lower()
            tmp = s[i][0].upper()
            s[i] = tmp + s[i][1:]

    print(' '.join(s))
    return ' '.join(s)


s = " A  sdf fFt "
solution(s)
