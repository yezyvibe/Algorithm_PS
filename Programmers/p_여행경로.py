from collections import defaultdict


def solution(tickets):
    tickets.sort(reverse=True)
    airport = defaultdict(list)
    for ticket in tickets:
        airport[ticket[0]].append(ticket[1])
    s = ['ICN']
    answer = []
    while s:
        top = s[-1]
        print(top)
        if top not in airport or len(airport[top]) == 0:
            answer.append(s.pop())
            print('1번', answer, airport)
        else:
            next = airport[top].pop()
            s.append(next)
            print('2번', next, s, airport)

    answer.reverse()
    return answer


tickets = [['ICN', 'A'], ['A', 'C'], ['A', 'D'], ['D', 'B'], ['B', 'A']]
print(solution(tickets))


# from collections import defaultdict
#
# def dfs(graph, N, key, footprint):
#     print(footprint)
#
#     if len(footprint) == N + 1:
#         return footprint
#
#     for idx, country in enumerate(graph[key]):
#         graph[key].pop(idx)
#
#         tmp = footprint[:]
#         tmp.append(country)
#
#         ret = dfs(graph, N, country, tmp)
#
#         graph[key].insert(idx, country)
#
#         if ret:
#             return ret
#
#
# def solution(tickets):
#     answer = []
#
#     graph = defaultdict(list)
#
#     N = len(tickets)
#     for ticket in tickets:
#         graph[ticket[0]].append(ticket[1])
#         graph[ticket[0]].sort()
#
#     answer = dfs(graph, N, "ICN", ["ICN"])
#
#     return answer