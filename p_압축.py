from string import ascii_uppercase
from collections import deque

def solution(msg):
    msg = deque(msg)
    dict = {}
    n = 1
    for i in ascii_uppercase:
        dict[i] = n
        n += 1
    
    answer = []
    now = ''
    while msg:
        now += msg.popleft()
        if len(msg) >= 1:
            tmp = now + msg[0]
        else:
            answer.append(dict[now])
            break
        if tmp in dict:
            continue
        else:
            answer.append(dict[now])  # 색인 번호 저장
            dict[tmp] = n  # 사전에 등록
            n += 1
            now = ''
    return answer