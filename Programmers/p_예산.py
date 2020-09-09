def solution(d, budget):
    d.sort()
    for i in range(len(d),0,-1):
        s = 0
        while s+i <= len(d):
            if sum(d[s:s+i]) <= budget:
                return i
            s += 1
    return 0