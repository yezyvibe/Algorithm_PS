from collections import deque


def solution(enter, leave):
    enter, leave = deque(enter), deque(leave)
    room = []
    next_enter = ''
    next_leave = ''
    answer = [0] * len(enter)

    while leave:       
        next_leave = leave.popleft()
        # 나갈 사람이 아직 room에 안 들어온 경우
        while next_leave not in room:
            next_enter = enter.popleft()
            room.append(next_enter)
        # 나갈 사람이 room에 들어있는 경우
        room.remove(next_leave)
        answer[next_leave-1] += len(room)
        for person in room:
            answer[person-1] += 1
    return answer
enter = [1,4,2,3]
leave = [2,1,3,4]
print(solution(enter, leave))