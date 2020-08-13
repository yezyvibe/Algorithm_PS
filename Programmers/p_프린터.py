from collections import deque
def solution(priorities, location):
    priorities = deque(priorities)
    l = len(priorities)
    result = [0]*l
    idx = 0
    cnt = 1
    while priorities:
        a = priorities.popleft()
        copy_lst = priorities.copy()
        for b in copy_lst:
            if a < b:
                priorities.append(a)
                idx += 1
                break
        else:
            result[idx] = cnt
            cnt += 1

            if idx+1 == l:
                idx = 0
            else:
                idx += 1

