def solution(lottos, win_nums):
    zero_cnt = lottos.count(0)   # 당첨 또는 낙첨될 수 있는 숫자들
    for i in range(zero_cnt):
        lottos.remove(0)

    res = 0
    for num in lottos:
        if num in win_nums:
            res += 1
    
    max_winning = 7 - zero_cnt - res
    min_winning = 7 - res
    
    if max_winning < 1:
        max_winning = 1
    elif max_winning > 6:
        max_winning = 6
    if min_winning > 6:
        min_winning = 6
    return [max_winning, min_winning]
