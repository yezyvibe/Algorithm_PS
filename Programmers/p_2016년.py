def solution(a, b):
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    weekday = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    day = sum(month[:a-1]) + b if a > 1 else b
    answer = weekday[day % 7-1]
    return answer