def solution(s):
    answer = ''
    s = s.split(' ')
    s = list(map(int, s))
    max_v = max(s)
    min_v = min(s)
    for num in s:
        if num > 0:
            if num > max_v:
                max_v = num
        else:
            if num < min_v:
                min_v = num
                print()
    answer = str(min_v) + ' ' + str(max_v)
    return answer

# def solution(s):
#     s = list(map(int,s.split()))
#     return str(min(s)) + " " + str(max(s))