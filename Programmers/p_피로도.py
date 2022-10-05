from itertools import permutations as permu

def solution(k, dungeons):
    L = len(dungeons)
    answer = 0
    for i in permu([i for i in range(L)], L):
        cur_fatigue = k
        cnt = 0
        for j in list(i):
            least_fatigue, exhaustion_fatigue = dungeons[j]
            if cur_fatigue >= least_fatigue:
                cur_fatigue -= exhaustion_fatigue
                cnt += 1
        answer = max(answer, cnt)
    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))