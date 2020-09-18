def solution(s):
    stack = []
    for i in range(len(s)):
        if not stack and s[i] == ')':
            return False
        if s[i] == '(':
            stack.append('(')
        else:
            if stack[-1] == '(':
                stack.pop()
            else:
                return False
    else:
        return False if stack else True

# def solution(s):
#     x = 0
#     for w in s:
#         print(w)
#         if x < 0:
#             break
#         x = x + 1 if w == "(" else x - 1 if w == ")" else x
#     return x == 0