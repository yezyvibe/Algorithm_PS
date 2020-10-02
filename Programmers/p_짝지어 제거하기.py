# 새로 짠 코드
def solution(s):
    if len(s) % 2 == 1:
        return 0

    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)

    if len(stack) == 0:
        return 1
    else:
        return 0

# 시간 초과 코드
def solution(s):
    if len(s) % 2 == 1:
        return 0

    set_s = set(s)
    for i in set_s:
        cnt = s.count(i)
        if cnt % 2 == 1:
            return 0

    idx = 0
    while True:
        if len(s) == 0:
            return 1
        if idx > len(s) - 2:
            return 0
        if s[idx] == s[idx + 1]:
            if idx == 0:
                s = s[idx + 2:]
            else:
                s = s[:idx] + s[idx + 2:]
                idx = 0
        else:
            idx += 1