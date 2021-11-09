import math 


def solution(n, words):
    words_dict = {}
    front = words[0]
    words_dict[front[0]] = [front]
    cnt = 0
    for i in range(1, len(words)):
        next = words[i]
        if front[-1] == next[0]:
            if next[0] not in words_dict:
                words_dict[next[0]] = [next]
            else:
                if next in words_dict[next[0]]:
                    cnt = i + 1
                    break
                else:
                    words_dict[next[0]].append(next)
            front = next
        else:
            cnt = i + 1
            break
    else:
        return [0, 0]
    order, num  =  cnt % n, math.ceil(cnt / n)
    if order == 0:
        order = n
    return [order, num]