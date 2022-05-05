import math

def toMinutes(time): 
    h, m = time.split(":")
    result = int(m)
    result += int(h) * 60
    return result 
    
def getTotalTime(r):
    in_tmp = 0
    result = 0
    if len(r) % 2 == 1:
        action, time = r.pop()
        result += (toMinutes("23:59") - toMinutes(time))

    for i in range(len(r)):
        action, time = r[i]
        time = toMinutes(time)
        if action == "IN":
            in_tmp = time
        elif action == "OUT":
            result += (time - in_tmp)
            in_tmp = 0
    return result

def solution(fees, records):
    # 차량별로 입출차 내역 정리하기 
    car_in_out = {}

    for i in range(len(records)):
        time, car_num, action = records[i].split(" ")
        if car_num in car_in_out:
            car_in_out[car_num].append([action, time])
        else:
            car_in_out[car_num] = [[action, time]]
            
    # 총 주차 시간 합산 & 요금표 참고하여 정산
    result = []
    for key, value in car_in_out.items():
        result.append([key, getTotalTime(value)])
    
    # 요금표 보고 정산하기
    answer = []
    for i in range(len(result)):
        car_num, time = result[i]
        payFee = 0
        if time > fees[0]:
            payFee += fees[1]
            payFee += (math.ceil((time - fees[0]) / fees[2]) * fees[3])
        else:
            payFee += fees[1]
        answer.append([car_num, payFee])
    answer.sort(key= lambda x : x[0])
    return [fee for _, fee in answer]


fees =[1, 461, 1, 10]
records = 	["00:00 1234 IN"]
print(solution(fees, records))