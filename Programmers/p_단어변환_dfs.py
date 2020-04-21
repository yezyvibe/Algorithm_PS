# bfs 개념 활용
def solution(begin, target, words):
    if target not in words:
        answer = 0
    elif begin in words:
        answer = 1
    else:
        result = {begin:0}
        stack = [begin]
        visit = [0] * len(words)
        while stack:
            begin = stack.pop(0)
            for word in words:
                cnt = 0
                for k in range(len(word)):
                    if word[k] != begin[k]:
                        cnt += 1
                    if cnt == 2:
                        break
                else:
                    idx = words.index(word)
                    if visit[idx] == 0:
                        visit[idx] = 1
                        stack.append(word)
                        result[word] = result[begin] + 1
                        if word == target:
                            break
        answer = result.get(target)
    return answer