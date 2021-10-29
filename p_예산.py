def solution(d, budget):
    if sum(d) <= budget:
        return len(d)
    d.sort()
    total = 0
    for i in range(len(d)):
        total += d[i]
        if total > budget:
            return i
            