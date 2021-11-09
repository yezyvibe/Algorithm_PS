from collections import deque

def solution(priorities, location):
    q = deque()
    for index,priority in enumerate(priorities):
        q.append((index, priority))

    cnt = 1
    while q:
        max_v = max(q, key=lambda x: x[1])
        index, docu_p = q.popleft()
        # print(max_v, index, docu_p)
        if max_v[1] <= docu_p:
            if index == location:
                return cnt
            cnt += 1
        else:
            q.append((index, docu_p))
    return cnt    
priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))