from collections import deque

def solution(numbers, target):
    
    q = deque([[numbers[0], 0], [-numbers[0], 0]])
    answer = 0
    while q:
        tmp, idx = q.popleft()
        idx += 1
        if idx < len(numbers):
            q.append([tmp+numbers[idx], idx])
            q.append([tmp-numbers[idx], idx])
        else:
            if tmp == target:
                answer += 1
    return answer