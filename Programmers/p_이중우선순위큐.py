import heapq


def solution(operations):
    num = []
    for i in operations:
        i = i.split()
        print(i[0])
        if i[0] == 'I':
            heapq.heappush(num, int(i[1]))
            print(num, '1번')
        elif i[1] == '1':
            try:
                num.pop()
                print(num, '2번')
            except:
                continue
        elif i[1] == '-1':
            try:
                heapq.heappop(num)
                print(num, '3번')
            except:
                continue
    if not num:
        return [0, 0]
    else:
        return [max(num), min(num)]


operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
print(solution(operations))

# q = [-10, 20, 10, -20]
# heapq.heappop(q)
# print(q)
