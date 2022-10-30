def solution(logs, events):
    user_dict = {}
    for i in range(len(logs)):
        cur = logs[i].split(" ")
        time, user, event = cur
        if user not in user_dict:
            user_dict[user] = [event]
        else:
            user_dict[user].append(event)

    answer = []
    for key, val in user_dict.items():
        idx = 0
        for i in range(len(val)):
            if val[i] == events[idx]:
                idx += 1
                if idx == len(events):
                    idx = 0
            else:
                answer.append(key)
                break
    answer.sort()
    return answer if len(answer) > 0 else ["-1"]