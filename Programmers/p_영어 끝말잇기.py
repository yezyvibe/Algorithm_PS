def solution(n, words):
    tmp = [words[0]] # 첫 번째 단어는 먼저 넣고 시작

    for i in range(1, len(words)): # 두 번째 단어부터 시작해서 끝말잇기 유효한지 확인
        if words[i - 1][-1] != words[i][0]: # 불가능한 경우 1번
            idx = i % n + 1
            cnt = i + 1
            break
        else:
            if words[i] not in tmp: # 가능한 경우
                tmp.append(words[i])
            else:                   # 불가능한 경우 2번
                idx = i % n + 1
                if idx == 0:
                    idx = n
                cnt = i + 1
                break
    else: # 주어진 단어 모두 탈락자가 생기지 않는 경우
        return [0, 0]

    if cnt % n == 0:
        cnt = cnt // n
    else:
        cnt = cnt // n + 1
    answer = [idx, cnt]
    return answer