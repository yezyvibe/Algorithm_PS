def solution(n, computers):
    visit = [0] * n
    answer = 0
    visit = [0] * n
    for i in range(n):
        if visit[i] == 0:
            s = [i]
            visit[i] = 1
            while s:
                x = s.pop()
                for k in range(n):
                    if visit[k] == 0 and computers[x][k] == 1:
                        s.append(k)
                        visit[k] = 1
            answer += 1
        if visit.count(1) == n:
            return answer
