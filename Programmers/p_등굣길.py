def solution(m, n, puddles):
    bg = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m+ 1):
            if i == 1 and j == 1: # 시작점
                bg[i][j] = 1
                print(bg)
                continue
            if [i, j] in puddles:
                bg[i][j] = 0
            else:
                bg[i][j] += (bg[i-1][j] + bg[i][j-1])
    return bg[n][m]
m = 4
n = 3
puddles = [[2,2]]
print(solution(m,n,puddles))
