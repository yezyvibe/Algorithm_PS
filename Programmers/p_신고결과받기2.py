def solution(id_list, report, k):
    report = list(set(report))
    reported_user = {}
    reporting_user = {}

    for id in id_list:
        reporting_user[id] = []

    for i in range(len(report)):
        reporterId, reportedId = report[i].split(" ")
        if reportedId in reported_user:
            reported_user[reportedId] += 1
        else:
            reported_user[reportedId] = 1
        
        if reportedId not in reporting_user[reporterId]:
            reporting_user[reporterId].append(reportedId)

    result = [0] * len(id_list)
    for i in range(len(id_list)):
        for reportedId in reporting_user[id_list[i]]:
            if reportedId in reported_user and reported_user[reportedId] >= k:
                result[i] += 1
    return result

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list, report, k))