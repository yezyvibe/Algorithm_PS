def solution(p):
    result = ""
    if p == "":
        return p
    # 전체가 올바른 괄호 문자열이면
    elif isRight(p) == True:
        return p
    else:
        # u, v로 문자열 나누기
        u, v = isBalance(p)
        # u가 올바른 괄호 문자열이면
        if isRight(u) == True:
            result += u
            result += solution(v)
            return result
        # u가 올바른 괄호 문자열이 아니면 False
        else:
            result += "("
            result += solution(v)
            result += ")"
            tmp = ""
            for i in u[1:-1]:
                if i == "(":
                    tmp += ")"
                else:
                    tmp += "("
            result += tmp
            return result

# 균형잡힌 괄호 문자열인지 판별하여, u랑 v 문자열 나누기
def isBalance(p):
    left_cnt = 0
    right_cnt = 0
    for i in p:
        if i == "(":
            left_cnt += 1
        else:
            right_cnt += 1
        if right_cnt != 0 and left_cnt == right_cnt:
            # u,v로 문자열 끊어주기
            idx = left_cnt + right_cnt
            u, v = p[0:idx], p[idx:]
            return u, v

# 올바른 괄호 문자열인지 판별
def isRight(p):
    tmp = []
    for i in p:
        if i == "(":
            tmp.append(i)
        else:
            if len(tmp) == 0:
                return False
            tmp.pop()
    if len(tmp) > 0:
        return False
    else:
        return True