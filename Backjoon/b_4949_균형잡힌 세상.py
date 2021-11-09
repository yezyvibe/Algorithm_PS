while True:
    string = input()
    stack = []
    answer = 'yes'
    if string == '.':
        break
    for s in string:
        if s == '(':
            stack.append('(')
        elif s == '[':
            stack.append('[')
        elif s == ')':
            if not len(stack):
                answer = 'no'
                break
            tmp = stack.pop()
            if tmp != '(':
                answer = 'no'
                break
        elif s == ']':
            if not len(stack):
                answer = 'no'
                break
            tmp = stack.pop()
            if tmp != '[':
                answer = 'no'
                break
    else:
        if len(stack):
            answer = 'no'
    print(answer)