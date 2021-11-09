from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    bridge = deque()
    total_weight = 0
    answer = 1 # 시간 재기
    while truck_weights or total_weight:
        answer += 1
        if truck_weights and weight >= truck_weights[0] + total_weight:
            now = truck_weights.popleft()
            bridge.append(now)
            total_weight += now
        else:
            bridge.append(0)  # 다리 위에 트럭을 올릴 수 없는 경우
        
        if len(bridge) == bridge_length:
            arrive = bridge.popleft()
            total_weight -= arrive
    return answer