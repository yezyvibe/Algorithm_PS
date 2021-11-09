def solution(dartResult):
    dartResult += '5'
    score_list = []
    score, index = 0, 0
    while index < len(dartResult):
        a = dartResult[index]
        if a.isdigit():
            if score:
                score_list.append(score)
                score = 0
            if a == '1' and dartResult[index+1] == '0':
                score += 10
                index += 1
            else:
                score += int(a)
        elif a == '#':
            score = -score
        elif a == '*':
            score = score * 2
            if score_list:
                score_list[-1] = score_list[-1] * 2
        else:
            if a == 'D':
                score = score ** 2
            elif a == 'T':
                score = score ** 3
        index += 1
    return sum(score_list)
dartResult = '1D2S#10S'
print(solution(dartResult))