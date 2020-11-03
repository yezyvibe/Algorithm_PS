from collections import defaultdict
import heapq


def solution(genres, plays):
    gen = defaultdict(list)
    cnt = defaultdict(int)
    for i in range(len(genres)):
        heapq.heappush(gen[genres[i]], (-plays[i], i))
        cnt[genres[i]] += plays[i]
    cnt_lst = []
    for k, v in cnt.items():
        cnt_lst.append((v, k))
    cnt_lst.sort(key=lambda x: -x[0])

    answer = []
    count = 0
    for item in cnt_lst:
        while gen[item[1]] and count < 2:
            song = heapq.heappop(gen[item[1]])
            tmp = song[1]
            answer.append(tmp)
            count += 1
        count = 0
    return answer
