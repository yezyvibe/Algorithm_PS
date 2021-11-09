def solution(s):
    stack = [s[0]]
    for i in range(1, len(s)):
        if not stack:
            stack.append(s[i])
        elif s[i] != stack[-1]:
            stack.append(s[i])
        else:
            stack.pop()
    if not stack:
        return 1
    return 0


s = 'cdcd'
print(solution(s))