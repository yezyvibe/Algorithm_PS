from collections import deque
import math

def solution(n, stations, w):
    stations = deque(stations)
    base_station = 0
    start = 1

    while stations:
        current = stations.popleft()
        end = current - w
        if start < end:
            spread = w * 2 + 1
            before = end - start
            base_station += math.ceil(before / spread)
        
        # 시작점 갱신
        start = current + w + 1
    
    # 끝까지 탐색이 되지 않은 경우
    if start <= n:
        before = n - (current + w)
        spread = w * 2 + 1
        base_station += math.ceil(before / spread)
    return base_station


print(solution(16, [9], 2))