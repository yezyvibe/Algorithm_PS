def dfs(airport_dict):
    s = ['ICN']
    visit_airport = []
    while s:
        now = s[-1]
        print(now)
        if now not in airport_dict or len(airport_dict[now]) == 0:
            visit_airport.append(s.pop())
        else:
            s.append(airport_dict[now].pop())
            print(s, 's')
    visit_airport.reverse()
    return visit_airport

def solution(tickets):
    tickets.sort(reverse=True)
    airport_dict = dict()
    for arrive, depart in tickets:
        if arrive in airport_dict:
            airport_dict[arrive].append(depart)
        else:
            airport_dict[arrive] = [depart]
    answer = dfs(airport_dict)
    return answer

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# tickets = [["ICN", "BBB"],["ICN", "CCC"],["BBB", "CCC"],["CCC", "BBB"],["CCC", "ICN"]]
# print(['ICN', 'BBB', 'CCC', 'ICN', 'CCC', 'BBB'])
print(solution(tickets))