def solution(cacheSize, cities):
    cache = []
    answer = 0
    for city in cities:
        city = city.upper()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            answer += 5
            if len(cache) == cacheSize:
                cache = cache[1:]
            if cacheSize == 0:
                continue
            cache.append(city)
    return answer

cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
print(solution(2,cities))