import heapq

def solution(operations):
    heap = []
    for op in operations:
        order, num  = op.split(' ')
        if order == 'I':
            heapq.heappush(heap, int(num))
        elif order == 'D' and heap:
            if num == '-1':
                heapq.heappop(heap)
            else:
                heap.sort()
                heap.pop()
    if heap:
        heap.sort()
        return [heap[-1], heap[0]]
    return [0, 0]
operations = ["I 1", "I 2", "I 3", "I 4", "I 5", "I 6", "I 7", "I 8", "I 9", "I 10", "D 1", "D -1", "D 1", "D -1", "I 1", "I 2", "I 3", "I 4", "I 5", "I 6", "I 7", "I 8", "I 9", "I 10", "D 1", "D -1", "D 1", "D -1"]
print(solution(operations))