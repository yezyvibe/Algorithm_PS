import math 

def jinsu(n, k):
    rev_base = ""
    while n > 0:
        n, r = divmod(n, k)
        rev_base += str(r)
    return rev_base[::-1]

def sosu(n):
    if n == 1: return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False # 소수 아니다
    return True # 소수이다

def solution(n, k):
    answer = 0
    changed = jinsu(n, k).split("0")
    changed = [i for i in changed if i]
    for i in range(len(changed)):
        ten_jinsu = int(changed[i])
        if sosu(ten_jinsu):
            answer += 1

    return answer

print(solution(437674, 3))