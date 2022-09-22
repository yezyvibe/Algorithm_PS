def solution(play_time, adv_time, logs):

    # 시간은 모두 초로 환산
    def convertToSeconds(string):
        h, m, s = string.split(":")
        all_seconds = int(s)
        all_seconds +=  int(h) * 60 * 60
        all_seconds += int(m) * 60
        return all_seconds

    viewers_arr = [0] * (convertToSeconds(play_time) + 1)
    adv_seconds =convertToSeconds(adv_time)

    for i in range(len(logs)):
        start, end = logs[i].split("-")
        start, end = [convertToSeconds(start), convertToSeconds(end)]
        viewers_arr[start] += 1
        viewers_arr[end] -= 1

    for i in range(1, len(viewers_arr)):
        viewers_arr[i] = viewers_arr[i-1] + viewers_arr[i]
    
    for i in range(1, len(viewers_arr)):
        viewers_arr[i] = viewers_arr[i-1] + viewers_arr[i]
    
    max_value = 0
    answer = 0
    for i in range(adv_seconds - 1, len(viewers_arr)):
        tmp = viewers_arr[i] - viewers_arr[i-adv_seconds]
        if i >= adv_seconds:
            if tmp > max_value:
                max_value = tmp
                answer = i - adv_seconds + 1
        else:
            if viewers_arr[i] > max_value:
                max_value = viewers_arr[i]
                answer = i - adv_seconds + 1
    
    h, r = divmod(answer, 3600)
    m, s = divmod(r, 60)
    return str(h).zfill(2) + ":"+ str(m).zfill(2) + ":"+ str(s).zfill(2)

play_time = "99:59:59"
adv_time = "25:00:00"
logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]

print(solution(play_time, adv_time, logs))