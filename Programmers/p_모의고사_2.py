def solution(answers):
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]

    res = [[1,0], [2,0], [3,0]]
    for i in range(len(answers)):
        if answers[i] == first[i % len(first)]:
            res[0][1] += 1
        if answers[i] == second[i % len(second)]:
            res[1][1] += 1
        if answers[i] == third[i % len(third)]:
            res[2][1] += 1
    
    target, max_cnt = [], 0
    for num, cnt in res:
            if cnt > max_cnt:
                max_cnt = cnt
                target = [num]
            elif cnt == max_cnt:
                target.append(num)
    return target
            


print(solution([1,3,2,4,2]))