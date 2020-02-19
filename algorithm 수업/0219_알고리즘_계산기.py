isp = {
    '*' : '2',
    '/': '2',
    '+': '1',
    '-':'1',
    '(':'0'
}
icp ={
    '*' : '2',
    '/': '2',
    '+': '1',
    '-':'1',
    '(':'3'
}
calc = '(6+5*(2-8)/2)'
s = ['(']
res = []
b = ''
for i in range(len(calc)):
    if calc[i].isdecimal():
        res.append(calc[i])
    else:
        if calc[i] == ')':
            while True:
                b = s.pop()
                if b == '(':
                    break
                res.append(b)
            continue

        if int(icp[calc[i]]) > int(isp[s[-1]]):
            s.append(calc[i])
        else:
            while int(icp[calc[i]]) <= int(isp[s[-1]]):
                a = s.pop()
                res.append(a)
            s.append(calc[i])

#연산하기
s2 = []
res2 = 0
for i in res:
    if i.isdecimal():
        s2.append(i)
    else:
        b = int(s2.pop())
        a = int(s2.pop())
        if i == '+':
            res2 = (a + b)
            s2.append(res2)
        elif i == '-':
            res2 = (a - b)
            s2.append(res2)
        elif i == '/':
            res2 = (a / b)
            s2.append(res2)
        else:
            res2 = (a * b)
            s2.append(res2)

result = s2.pop()
print(result)