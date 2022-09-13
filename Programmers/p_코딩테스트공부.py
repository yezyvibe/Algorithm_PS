def solution(alp, cop, problems):
    # 목표 알고력, 목표 코딩력 구하기
    max_alp = 0
    max_cop = 0
    for i in range(len(problems)):
        max_alp = max(problems[i][0], max_alp)
        max_cop = max(problems[i][1], max_cop)

    INF = float('inf')
    dp = [[INF] * (max_cop + 1) for _ in range(max_alp + 1)]
    alp, cop = min(max_alp, alp), min(max_cop, cop)
    dp[alp][cop] = 0 # 초기 시작
    
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if i + 1 <= max_alp: 
                dp[i+1][j] = min(dp[i][j] + 1, dp[i+1][j])
            if j + 1 <= max_cop:
                dp[i][j+1] = min(dp[i][j] + 1, dp[i][j+1])

            for alp_req, cop_rep, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_rep:
                    next_alp, next_cop = min(max_alp, i+alp_rwd), min(max_cop, j+cop_rwd)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + cost)

    return dp[max_alp][max_cop]


alp, cop, problems = 10, 10, [[10,15,2,1,2],[20,20,3,3,4]]
print(solution(alp, cop, problems))