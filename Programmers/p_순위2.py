def dfs(start, adj, n):
    visit = [0] * (n+1)
    stack = [start]
    visit[start] = 1

    while stack:
        cur = stack.pop()
        if cur not in adj:
            continue
        for k in adj[cur]:
            if not visit[k]:
                visit[k] = 1
                stack.append(k)
    visit[start] = 0
    return sum(visit)

def solution(n, results):
    win_dic = {} # key가 이긴 사람들을 value로 저장
    lose_dic = {}
    for winner, loser in results:
        if winner in win_dic:
            win_dic[winner].append(loser)
        else:
            win_dic[winner] = [loser]
        
        if loser in lose_dic:
            lose_dic[loser].append(winner)
        else:
            lose_dic[loser] = [winner]
            
    answer = 0
    for i in range(1, n+1):
        result = 0
        if i in win_dic:
            result += dfs(i, win_dic, n) 
        if i in lose_dic:
            result += dfs(i, lose_dic, n)
        if result == n - 1:
            answer += 1
    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))