def solution(brown, red):
    for sero in range(1, int(red**0.5)+1):    # 카펫의 가로 길이>= 세로 길이므로 범위 red**0.5
        if red % sero == 0:
            garo = red // sero
            if (sero + garo) * 2 + 4 == brown:
                return [garo + 2, sero + 2]