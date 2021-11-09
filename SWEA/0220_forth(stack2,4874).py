t = int(input())

for tc in range(1,t+1):
    forth = list(map(str, input().split()))
    s = []
    o = []
    for f in forth:
        if f.isdecimal():
            s.append(f)
        else:
            o.append(f)
# 숫자, 연산자 스택 완료
    try:
        for i in range(len(o)-1):
            if len(s) == 1 or len(s) == 0:
                result = 'error'
                break
            else:
                b = int(s.pop())
                a = int(s.pop())
                if o[i] == '+':
                    c = a + b
                    s.append(c)
                elif o[i] == '-':
                    c = a - b
                    s.append(c)
                elif o[i] == '*':
                    c = a * b
                    s.append(c)
                else:
                    c = a // b
                    s.append(c)
                result = c
        print(result)

    except:
        print('error')