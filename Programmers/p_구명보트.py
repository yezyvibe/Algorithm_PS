def solution(people, limit):
    people.sort(reverse=True)
    start, end = 0, len(people)-1
    cnt = len(people) # 전체 사람 수만큼 보트의 개수를 잡고, 두명씩 타는 경우가 생기면 -1씩 빼준다
    while start < end: # while문 종료조건, start와 end의 인덱스가 같아지면 무게를 비교할 필요가 없다
        if people[start] + people[end] <= limit:
            end -= 1 # 두명이 같이 타는 경우가 생기면 end의 인덱스를 한칸 앞으로 변경
            cnt -= 1
        start+= 1
    return cnt