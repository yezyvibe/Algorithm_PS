def solution(lines):  
    # 시작, 완료 시간 순서로 로그 데이터 저장
    start_complete_data = []
    for line in lines:
        # 시간을 밀리세컨드로 환산하기
        tmp = line.split(" ")
        time = tmp[1].split(":")
        h, m, s = time[0], time[1], time[2].split(".")[0]

        converted_time = (int(h)*60*60 + int(m)*60 + int(s)) * 1000 + int(time[2].split(".")[1])
        processing_seconds = int(float(tmp[2][:-1]) * 1000)
        start_complete_data.append((converted_time - processing_seconds + 1, converted_time))
    
    answer = 0
    for i in range(len(start_complete_data)):
        current = start_complete_data[i][1]
        throughput = 1

        for j in range(i+1, len(start_complete_data)):
            if start_complete_data[j][0] - 1000 < current:
                throughput += 1
        answer = max(answer, throughput)
    return answer

lines = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]
print(solution(lines))