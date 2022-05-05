# 15분
def solution(id_list, report, k):
    user_report = {} #유저별 신고한 아이디 목록 저장
    report_cnt = {} # 유저별 신고 받은 횟수 저장

    for i in range(len(id_list)):
        user_report[id_list[i]] = []
    
    for i in range(len(report)):
        from_user, to_user = report[i].split(" ")
        if to_user not in user_report[from_user]:
            user_report[from_user].append(to_user)
            if to_user in report_cnt:
                report_cnt[to_user] += 1
            else:
                report_cnt[to_user] = 1

    stopped_users = []
    for key, value in report_cnt.items():
        if value >= k:
            stopped_users.append(key)
    result = []
    for key, value in user_report.items():
        cnt = 0
        for i in range(len(value)):
            if value[i] in stopped_users:
                cnt += 1
        result.append(cnt)
    return result

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))

