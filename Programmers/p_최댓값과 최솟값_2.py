def solution(s):
    s = list(map(int, s.split(' ')))
    s.sort()
    answer = str(s[0]) +' '+ str(s[-1])
    return answer

s = "-1 -2 -3 -4"
print(solution(s))