def solution(gems):
    min_v = len(gems) + 1
    start_point = 0
    end_point = 0
    kinds_cnt = len(set(gems))
    gems_dict = {}

    while end_point < len(gems):
        if gems[end_point] not in gems_dict:
            gems_dict[gems[end_point]] = 1
        else:
            gems_dict[gems[end_point]] += 1
        end_point += 1

        if len(gems_dict) == kinds_cnt:
            while start_point < end_point:
                if gems_dict[gems[start_point]] > 1:
                    gems_dict[gems[start_point]] -= 1
                    start_point += 1
                else:
                    if min_v > end_point - start_point:
                        min_v = end_point - start_point
                        answer = [start_point+1, end_point]
                    break
    return answer
gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))
