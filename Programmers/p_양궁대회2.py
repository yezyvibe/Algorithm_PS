def getPoint(ryan_round, apeach_round):
    ryan_point, apeach_point = 0, 0
    for i in range(len(ryan_round)):
        if ryan_round[i] == "1":
            ryan_point += (10 - i)
        elif int(apeach_round[i]):
            apeach_point += (10 - i)
    return [ryan_point, apeach_point]


def isPossibleToGetPoint(leftover_arrow, ryan_round, apeach_round):
    for i in range(len(ryan_round)):
        if ryan_round[i] == "1": # 이기는 경우
            leftover_arrow -= (int(apeach_round[i]) + 1) # 점수를 획득하기 위해서 어피치 보다 1발을 더 많이 싸야 한다.
            if leftover_arrow < 0:
                return [False, ""] # 불가능한 케이스

    ryan_round = ryan_round.ljust(11, "0")
    return [True, ryan_round]

def solution(n, info):
    cur = ""
    max_v = 0
    cases = ["0", "1"] # 0 지거나 1 이기거나
    info = "".join(map(str,info))
    possible = set()
    def dfs(idx, cur, info, n):
        nonlocal max_v, possible
        if idx == 11:
            return
        for case in cases:
            next = cur + case
            result = isPossibleToGetPoint(n, next, info)
            if result[0]:
                ryan, apeach = getPoint(result[1], info)
                gap = ryan - apeach
                if gap > 0: # 비기는 경우는 라이언이 지는 경우이기 때문에 포함x
                    if max_v < gap:
                        max_v = gap
                        possible = set([result[1]])
                    elif max_v == gap:
                        possible.add(result[1])
            dfs(idx+1, next, info, n)
    dfs(0, cur, info, n)
    possible = list(possible)

    if not possible: return [-1]
    if len(possible) > 1 :
        for i in range(10, -1, -1):
            tmp = []
            for j in range(len(possible)):
                if possible[j][i] == "1":
                    tmp.append([j, i, possible[j][i]])
            if tmp:
                tmp.sort(key=lambda x: x[2])
                possible = [possible[tmp[-1][0]]]
                break

    answer = []
    for i in range(11):
        if i == 10 and int(possible[0][i]) > 1:
            answer.append(int(possible[0][i]))
            continue
        if possible[0][i] == "1":
            answer.append(int(info[i]) + 1)
        else:
            answer.append(0)

    ryan_total = sum(answer)
    if ryan_total < n: # 남은 화살의 개수만큼 맨 뒤 점수에 더해주기
        answer[-1] += (n - ryan_total)
    return answer