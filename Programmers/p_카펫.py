def solution(brown, yellow):
    answer = []
    cnt = 1
    while True:
        if cnt == 1:
            y_g = yellow // cnt
            y_s = 1
        else:
            y_g = yellow // cnt
            y_s = cnt
        b = ((y_g+2)+(y_s))*2
        if b == brown and (y_g*y_s) == yellow:
            return [y_g+2, y_s+2]
        cnt += 1