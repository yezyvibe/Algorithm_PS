t = int(input())

for tc in range(1, t+1):
    stack = []
    words = list(input())
    result = 1
    for word in words:
        if word == '(' or word =='{':
            stack.append(word)
        if word ==')' or word == '}':
            if stack != []:
                a = stack.pop() # 끝에서부터 하나 꺼내오기
                if a == '{':
                    if word != '}':
                        result = 0
                        break
                elif a == '(':
                    if word != ')':
                        result = 0
                        break
            else:
                result = 0
                break
    if stack != []:
        result = 0
    print('#{} {}'. format(tc, result))