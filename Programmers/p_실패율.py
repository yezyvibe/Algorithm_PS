def solution(N, stages):
    answer = []
    result = []
    users = len(stages)
    for i in range(1,N+1):
        cnt = stages.count(i)
        if cnt != 0:
            fail = cnt/users
            answer.append((fail, i))
        else:
            fail = 0
            answer.append((fail, i))
        users -= cnt
    answer = sorted(answer, key = lambda x: (-x[0],x[1]))
    for a, b in answer:
        result.append(b)
    return result

# 딕셔너리로 푼 경우
# return sorted(result, key=lambda x : result[x], reverse=True)