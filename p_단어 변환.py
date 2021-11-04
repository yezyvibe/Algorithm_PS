# bfs 로직으로 풀것임

from collections import deque


def bfs(begin, target, words, visit):
    q = deque([[begin, 0]])
    
    while q:
        now, depth = q.popleft()
        if now == target:
            return depth

        for i in range(len(words)):
            if visit[i]:
                continue
            cnt = 0
            for j in range(len(now)):
                if now[j] != words[i][j]:
                    cnt += 1
                    if cnt > 1:
                        break
            else:
                visit[i] = 1
                q.append((words[i], depth+1))


def solution(begin, target, words):
    answer = 0
    visit = [0]*len(words)
    if target not in words:
        return answer
    answer = bfs(begin, target, words, visit)    
    return answer

begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))