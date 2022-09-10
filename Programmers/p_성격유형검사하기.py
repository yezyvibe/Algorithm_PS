def solution(survey, choices):
    charactors_dict = {
        'R': 0,
        'T': 0,
        'C': 0,
        'F': 0,
        'J': 0,
        'M': 0,
        'A': 0,
        'N': 0,
    }
    # 모든 질문의 성격 유형 점수 계산
    for i in range(len(survey)):
        current_question = survey[i]
        current_answer = choices[i]
        default_score = 4
        if current_answer < default_score:
            charactors_dict[current_question[0]] += (default_score - current_answer)
        elif default_score < current_answer <= 7:
            charactors_dict[current_question[1]] += (current_answer - default_score)

    # 점수 비교로 성격 유형 최종 결정하기
    before_charactor = ''
    before_charactor_score = 0
    cnt = 0
    result = ''
    for key, val in charactors_dict.items():
        cnt += 1
        if cnt != 2:
            before_charactor = key
            before_charactor_score = val
            continue
        
        if before_charactor_score > val:
            result += before_charactor
        elif before_charactor_score < val:
            result += key
        elif before_charactor_score == val:
            result += sorted([key, before_charactor])[0]
        cnt = 0

    return result

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
print(solution(survey, choices))