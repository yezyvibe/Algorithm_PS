def solution(N, stages):
    answer = []
    stages.sort()
    for i in range(1, N+1):
        fail_user = stages.count(i)
        total_user = len(stages)
        if total_user:
            answer.append((fail_user/total_user, i))
        else:
            answer.append((0, i))
        while fail_user > 0:
            stages.remove(i)
            fail_user -= 1
    answer.sort(key=lambda x:(-x[0], x[1]))
    return [stage for rate, stage in answer]

N = 5
stages = [1,2,2,1,3]
print(solution(N, stages))


# 1,6,7,9,13,23,24,25 런타임에러 -> total_user 가 0인 경우 fail_user를 0으로 나누게 되면 ZeroDivisionError가 
# 발생한다.