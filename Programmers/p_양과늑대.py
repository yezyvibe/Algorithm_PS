def solution(info, edges):
    visit = [0] * len(info)
    visit[0] = 1
    answer = 0

    def dfs(sheep, wolf):
        nonlocal answer
        if sheep > wolf:
            answer = max(answer, sheep)
        else:
            return
        for i in range(len(edges)):
            parent, child = edges[i]
            isWolf = info[child]
            if visit[parent] and not visit[child]:
                visit[child] = 1
                dfs(sheep + (isWolf^1), wolf + (isWolf))
                visit[child] = 0
    dfs(1, 0)
    return answer

info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges =  [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
print(solution(info, edges))