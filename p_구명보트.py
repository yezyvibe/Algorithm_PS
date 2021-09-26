def solution(people, limit):
    people.sort()
    answer = 0
    s, e = len(people)-1, 0

    while e <= s:
        if people[s] + people[e] <= limit:
            s -= 1
            e += 1
        else:
            s -= 1
        answer += 1
    return answer



people = [70, 50, 80, 50]
limit = 100
print(solution(people, limit))