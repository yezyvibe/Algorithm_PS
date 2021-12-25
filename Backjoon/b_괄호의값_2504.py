brackets = input()
s = []
chk = 0
for i in brackets:
    if not s:
        if i in [')', ']']:
            print(0)
            exit(0)
            
    if i == ')':
        tmp = 0
        while s:
            top = s.pop()
            if top == '(':
                if tmp == 0:
                    s.append(2)
                else:
                    s.append(tmp*2)
                break
            elif top == '[':
                print(0)
                exit(0)
            else:
                tmp += int(top)
        
    elif i == ']':
        tmp = 0
        while s:
            top = s.pop()
            if top == '[':
                if tmp == 0:
                    s.append(3)
                else:
                    s.append(tmp*3)
                break
            elif top == '(':
                print(0)
                exit(0)
            else:
                tmp += int(top)
                
    else:
        s.append(i)

try:
    print(sum(s))
except:
    print(0)      