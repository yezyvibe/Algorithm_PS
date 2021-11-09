for i in range(int(input())):
    lst = list(map(str, input()))
    s = []

    for i in lst:
        if len(s) == 0:
            if i == ')':
                res = 'NO'
                break
            else:
                s.append(i)
        elif i == ')':
            if s[-1] == '(':
                s.pop()
        else:
            s.append(i)
    else:
        if len(s) != 0:
            res = 'NO'
        else:
            res = 'YES'
    print(res)