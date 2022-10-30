def solution(cap, n, deliveries, pickups):
    answer = 0
    
    d_pointer, p_pointer = n - 1, n - 1
    while True:
        move_cnt = 0

        # 1. 배달하기
        truck = 0
        is_last_pointer = False
        for i in range(d_pointer, -1, -1):
            item = deliveries[i]
            # 배달할 택배가 있는 경우
            if item > 0:
                if is_last_pointer is False:
                    move_cnt += i + 1
                    is_last_pointer = True

                if truck + item <= cap:
                    truck += item
                    deliveries[i] = 0
                else:
                    deliveries[i] -= (cap - truck)
                    d_pointer = i
                    break

        # 2. 수거하기
        truck = 0
        is_last_pointer = False
        for i in range(p_pointer, -1, -1):
            item = pickups[i]
            # 수거할 택배가 있는 경우
            if item > 0:
                if is_last_pointer is False:
                    move_cnt = max(move_cnt, i + 1)
                    is_last_pointer = True

                if truck + item <= cap:
                    truck += item
                    pickups[i] = 0
                else:
                    # 남은 수만큼만 빼가자
                    pickups[i] -= (cap - truck)
                    p_pointer = i
                    break
        
        # 더 이상 움직일 필요가 없으면 종료
        if move_cnt == 0:
            break
        
        answer += move_cnt * 2

    return answer