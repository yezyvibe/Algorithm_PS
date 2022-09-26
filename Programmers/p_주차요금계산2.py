from math import ceil

def solution(fees, records):
    basic_time, basic_rate, unit_time, unit_rate = fees
    car_dict = {}

    def convert_time(str):
        # 분단위로 모두 환산
        h, m = str.split(":")
        return int(m) + (int(h) * 60)

    for i in range(len(records)):
        time, car_num, inOut =records[i].split(" ")
        if car_num in car_dict:
            car_dict[car_num].append([inOut, convert_time(time)])
        else:
            car_dict[car_num] = [[inOut, convert_time(time)]]
    
    answer = []
    for key, value in car_dict.items():
        total_time = 0
        next_time = 0
        total_fee = 0
        while value:
            inOut, cur_time = value.pop()
            if inOut == 'OUT':
                next_time = cur_time
            elif inOut == 'IN':
                if next_time == 0:
                    next_time = convert_time("23:59")    
                total_time += (next_time - cur_time)
                next_time = 0
        
        if total_time <= basic_time:
            answer.append([key, basic_rate])
        else:
            # 기본 시간 초과하는 경우
            total_time -= basic_time
            total_fee += basic_rate
            total_fee += ceil(total_time / unit_time) * unit_rate
            answer.append([key, total_fee])
    
    answer.sort(key=lambda x:x[0])
    return [f for n, f in answer]
    
fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))