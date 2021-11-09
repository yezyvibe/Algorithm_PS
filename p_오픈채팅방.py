def solution(records):
    id_name_dict = {}
    results = []
    answer = []
    for record in records:
        record_lst = record.split(' ')
        if record_lst[0] != "Leave":
            if record_lst[1] not in id_name_dict:
                    id_name_dict[record_lst[1]] = record_lst[2]
            else:
                id_name_dict[record_lst[1]] = record_lst[2]
        if record_lst[0] != "Change":
            results.append((record_lst[1], record_lst[0]))
    
    for result in results:
        if result[1] == "Enter":
            tmp = "들어왔습니다."
        else:
            tmp = "나갔습니다."
        answer.append(id_name_dict[result[0]] + "님이 " + tmp)
    
    return answer
        
records = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(records))