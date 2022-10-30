def solution(sx1, sy1, sx2, sy2, sticks):
    answer = 0
    for stick in sticks:
        a, b, c, d = stick
        if sx1 < a < sx2 and sy1 < b < sy2:
            if sx1 < c < sx2 and sy1< d < sy2:
                answer += 1
    return answer