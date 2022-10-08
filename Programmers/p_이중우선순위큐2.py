import heapq

def solution(operations):
    min_hq = []
    max_hq = []
    for i in range(len(operations)):
        current = operations[i]
        op, num = current.split(" ")
        if op == "I":
            heapq.heappush(min_hq, int(num))
            heapq.heappush(max_hq, -int(num))
        elif op == 'D' and num == '1' and len(max_hq) > 0:
            max_v = heapq.heappop(max_hq)
            min_hq.remove(-max_v)
        elif op == 'D' and num == '-1'and len(min_hq) > 0:
            min_v = heapq.heappop(min_hq)
            max_hq.remove(-min_v)
    if not min_hq and not max_hq:
        return [0, 0]
    min_v = heapq.heappop(min_hq)
    max_v = heapq.heappop(max_hq)
    return [-max_v, min_v]
            

operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
print(solution(operations))