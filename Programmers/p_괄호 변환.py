def separation(p):
    left_bracket = 0
    right_bracket = 0
    for i in range(len(p)):
        if p[i] == '(':
            left_bracket += 1
        else:
            right_bracket += 1
        if left_bracket == right_bracket:
            return p[:i+1], p[i+1:]

def correct(p):
    tmp = []
    for i in p:
        if not tmp:
            tmp.append(i)
        else:
            if i == ')':
                if tmp[-1] == '(':
                    tmp.pop()
                else:
                    return False
            else:
                tmp.append(i)
    if not tmp:
        return True
    else:
        return False

def change(p):
    tmp = ''
    for i in p:
        if i == '(':
            tmp += ')'
        else:
            tmp += '('
    return tmp

def solution(p):
    if p == '':
        return ''
    u, v = separation(p)
    answer = '('
    if correct(u): # 올바른 괄호 문자열인 경우
        return u + solution(v)
    else: # 올바른 괄호가 아닌 경우
        answer += solution(v)
        answer += ')'
        answer += change(u[1:-1])
        return answer