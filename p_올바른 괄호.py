def solution(s):
    stack = []
    for i in s:
        if i == ')':
            if not stack:
                return False
            if stack[-1] == '(':
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
    else:
        if stack:
            return False
        else:
            return True