from collections import deque
def solution(priorities, location):
    answer = 0
    array = deque([(v, i) for i, v in enumerate(priorities)])

    while len(array):
        item = array.popleft()
        if array and max(array)[0] > item[0]:
            array.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer