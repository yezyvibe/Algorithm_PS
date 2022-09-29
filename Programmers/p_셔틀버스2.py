def convert_to_minutes(time):
    h, m = time.split(":")
    return int(h) * 60 + int(m)

def convert_to_origin(time):
    q, r = divmod(time, 60)
    return str(q).zfill(2) + ":" +str(r).zfill(2)

def solution(n, t, m, timetable):
    # 버스 스케줄표 먼저 만들어 놓기
    bus_time_table = []
    start_time = convert_to_minutes("09:00")
    for i in range(n):
        next_time = start_time + (i * t)
        bus_time_table.append(next_time)
    
    # 크루들의 도착 시간표 -> 분으로 모두 통일해서 담기
    for i in range(len(timetable)):
        timetable[i] = convert_to_minutes(timetable[i])
    timetable.sort()

    # 버스 하나씩 순서대로 태울 때 마지막 버스에 콘이 탈 수 있도록 도착 시간 찾기
    bus_dict = {} # 버스 별로 가장 마지막에 탄 크루의 시간만 저장하고 있기
    for i in range(len(bus_time_table)):
        bus_dict[bus_time_table[i]] = []

    for i in range(len(timetable)):
        cur = timetable[i]
        for key, val in bus_dict.items():
            if cur <= key and len(val) < m:
                # 탈 수 있다
                bus_dict[key].append(cur)
                break
    
    last_bus = bus_time_table[-1]
    if len(bus_dict[last_bus]) < m:
        answer = last_bus
    else:
        answer = bus_dict[last_bus][-1] - 1
    return convert_to_origin(answer)


print(solution(	2, 10, 2, ["09:10", "09:09", "08:00"]))