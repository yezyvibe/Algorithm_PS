def solution(clothes):
    clothes_dic = {}
    cnt = 1
    for i in clothes:
        tmp = i[1]
        if clothes_dic.get(tmp):
            clothes_dic[tmp] += 1
        else:
            # 선택하지 않는 경우도 포함하기 위해 1을 더해 2부터 값 넣기
            clothes_dic[tmp] = 2
    for i in clothes_dic.values():
        cnt *= i
    return cnt - 1
