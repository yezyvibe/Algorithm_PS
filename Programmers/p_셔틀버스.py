def solution(n, t, m, timetable):
    # 운행 횟수 n, t분마다, m명까지 탈 수 있다.
    # 다른 크루가 타든 안 타든 상관 없다는 마인드
    # 크루 도착 시간 분으로 통일
    timetable.sort(reverse=True)
    crews = []
    for time in timetable:
        time = list(map(int, time.split(":")))
        time = time[0] * 60 + time[1]
        crews.append(time)
        
    # 모두 분으로 통일하여 버스 스케줄표 만들기
    bus_schedule = []
    start_time = 9*60
    for _ in range(n):
        bus_schedule.append((start_time, []))
        start_time += t
    
    for i in range(len(bus_schedule)):
        cnt = 0
        while cnt < m and crews:
            if crews[-1] <= bus_schedule[i][0]:
                bus_schedule[i][1].append(crews.pop())
                cnt += 1
            else:
                break

    # 콘이 제일 마지막 버스를 탈 수 있게
    last_bus = bus_schedule[-1]
    if len(last_bus[1]) < m:   # 다른 크루들과 함께 콘이 탈 수 있는 경우
        answer = last_bus[0]
    else:                      # 마지막 크루 한명을 제외하고 콘이 타야 하는 경우
        last_bus[1].sort()
        last_crew = last_bus[1][-1]
        answer = last_crew - 1

    h, m = divmod(answer, 60)
    con = str(h).zfill(2) + ":" + str(m).zfill(2)
    return con

n, t, m = 2, 1, 2
timetable = ["09:00", "09:00", "09:00", "09:00"]
print(solution(n, t, m, timetable))