from itertools import permutations as permu

def solution(k, dungeons):
    max_v = 0
    for p in permu(range(len(dungeons)),len(dungeons)):
        cnt = 0
        initial_k = k
        for i in p:
            least, consumption = dungeons[i]
            if least <= initial_k:
                initial_k -= consumption
                cnt += 1
                print(least, consumption)
        else:
            max_v = max(max_v, cnt)
    return max_v

k = 80
dungeons = [[80,20],[50,40],[30,10]]
print(solution(k, dungeons))