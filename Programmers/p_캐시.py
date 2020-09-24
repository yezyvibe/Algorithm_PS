from collections import deque

def solution(cacheSize, cities):
    answer = 0
    buffer = deque()

    if cacheSize == 0:
        return 5 * len(cities)

    for city in cities:
        city = city.lower()
        if city not in buffer:
            if len(buffer) == cacheSize:
                buffer.popleft()
            buffer.append(city)
            answer += 5
        else:
            buffer.remove(city)
            buffer.append(city)
            answer += 1

    return answer