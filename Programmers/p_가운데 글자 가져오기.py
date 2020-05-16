def solution(s):
    if len(s) % 2 == 1:
        # 홀수
        idx = len(s)//2
        answer = s[idx]
    else:
        idx = len(s)//2
        answer = s[idx-1:idx+1]
    return answer