def solution(skill, skill_trees):
    skill = list(skill)
    answer = 0
    for skill_tree in skill_trees:
        check = [0] * len(skill)
        idx = 1
        for i in skill_tree:
            if i in skill:
                check[skill.index(i)] = idx
                idx += 1

        front = 0
        zero_check = 0
        for k in check:
            if k == 0:
                zero_check = 1
                continue
            if zero_check == 1:
                break
            if k and front > k:
                break
            front = k
        else:
            answer += 1
     
    return answer


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))