def dfs(visit,computers, i, cnt):
    stack = [i]
    while stack:
        a = stack.pop()
        for j in range(len(computers)):
            if computers[a][j] == 1 and not visit[j]:
                stack.append(j)
                visit[i] = cnt

    return visit


def solution(n, computers):
    visit = [0]*n
    cnt = 1
    for i in range(n):
        if not visit[i]:
            dfs(visit, computers, i, cnt)
            cnt += 1
    return cnt-1

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))