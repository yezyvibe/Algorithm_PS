# pi배열 구하는 함수
# pi[i]는 주어진 문자열의 0~i 까지의 부분 문자열 중에서
# prefix == suffix가 될 수 있는 부분 문자열 중에서 가장 긴 것의 길이
def searchPi(p):
    pi = [0] * len(p)
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = pi[j - 1]
        if p[i] == p[j]:
            j += 1
            pi[i] = j
    return pi


def KMP(s, p):
    pi = searchPi(p)
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = pi[j - 1]
        if s[i] == p[j]:
            if j == len(p) - 1:
                return True
            else:
                j += 1
    return False


s = input()
p = input()

print(1 if KMP(s, p) else 0)
