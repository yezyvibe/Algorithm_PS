# 완전 탐색, dfs -> 단, 더 높은 점수가 될 수 없을 때는 탐색 종료

# 점수로 라이언이 > 어피치를 이기는지 확인
def calculateScore(ryan, appeach):
    ryan_score = 0
    appeach_score = 0
    for i in range(len(ryan)):
        if ryan[i]:
            ryan_score += (10 - i)
        elif appeach[i]:
            appeach_score += (10 - i)
    return [True, ryan_score - appeach_score] if ryan_score > appeach_score else [False, -1]

# 남은 화살 있는지 확인
def isRemainArrows(ryan, appeach, n):
    ryan_arrows_cnt = 0
    for i in range(len(ryan)):
        if ryan[i]:
            ryan_arrows_cnt += (appeach[i] + 1)
            if ryan_arrows_cnt > n:
                # 화살 부족으로 -> 불가
                return False
    return True

def getResult(ryan_arrows, appeach_arrows, n):
    total = 0
    for i in range(len(ryan_arrows)):
        if ryan_arrows[i]:
            ryan_arrows[i] = appeach_arrows[i] + 1
            total += (appeach_arrows[i] + 1)
    if total < n:
        ryan_arrows[-1] += (n-total)
    return ryan_arrows

def solution(n, info):
    idx = 0
    ryan_arrows = [0] * 11
    candidates = set([])
    max_gap = 0
    def dfs(ryan_arrows, appeach_arrows, idx, n):
        nonlocal max_gap, candidates
        if idx > 10:
            return
        if not isRemainArrows(ryan_arrows, appeach_arrows, n):
            return
        result, gap = calculateScore(ryan_arrows, appeach_arrows)
        if result:
            if gap > max_gap:
                max_gap = gap
                candidates = set([tuple(ryan_arrows)])
            
            elif gap == max_gap:
                candidates.add(tuple(ryan_arrows))
            # 정답 후보로 넣기
        
        # 해당 점수를 따거나(어피치 보다 1 많이 화살 맞춤) 버리거나(0)
        dfs(ryan_arrows, appeach_arrows, idx + 1, n)
        ryan_arrows[idx] = 1
        dfs(ryan_arrows, appeach_arrows, idx + 1, n)
        ryan_arrows[idx] = 0

    dfs(ryan_arrows, info, idx, n)
    candidates = list(candidates)

    if len(candidates) == 1:
        return getResult(list(candidates[0]), info, n)
    elif len(candidates) == 0:
        return [-1]

    candidates = list(map(list, candidates))
    changed_candidates = []
    for i in range(len(candidates)):
        changed_candidates.append(getResult(candidates[i], info, n))

    max_v = 0
    answer = []
    for i in range(len(candidates[0])-1, -1, -1):
        for j in range(len(candidates)):
            if candidates[j][i]:
                if max_v < candidates[j][i]:
                    max_v = candidates[j][i]
                    answer = [candidates[j]]
                elif max_v == candidates[j][i]:
                    answer.append(candidates[j])
        if answer:
            break
    answer = answer[0]

    total = sum(answer)
    if total < n:
        answer[-1] += (n-total)
    return answer



n = 9
info = [0,0,1,2,0,1,1,1,1,1,1]
print(solution(n, info))