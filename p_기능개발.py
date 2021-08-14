import math

def solution(progresses, speeds):
    answer = []
    tmp = []
    for i in range(len(progresses)):
        p, s = progresses[i], speeds[i]
        r = math.ceil((100 - p) / s)
        tmp.append(r)

    before = tmp[0]
    cnt = 1
    for i in range(1, len(tmp)):
        print(tmp[i])
        if before >= tmp[i]:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            before = tmp[i]
    answer.append(cnt)
    return answer 
     
progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses,speeds))