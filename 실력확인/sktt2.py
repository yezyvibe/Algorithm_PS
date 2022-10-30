from itertools import product


def solution(receive, sell):
    # 일반 판매 끝나고 재고만 구매
    # 일반 판매 수요가 > 재고 -> 재고까지 판매

    L = len(receive) # 매장 개수
    cases = list(product([i for i in range(L)], repeat=5))

    max_buy = 0
    result = []
    for i in range(len(cases)):
        case = list(cases[i])
        stock = [0] * L  # 각 스토어별 재고량    
        buy = 0  # 구매량
        for j in range(5):
            # 날짜 하루씩 지나면서 체크 -> 재고량 저장
            for k in range(L): # 모든 매장 돌기
                cur_stock = (stock[k] + receive[k][j] - sell[k][j])
                if cur_stock < 0:
                    cur_stock = 0
                stock[k] = cur_stock

            store = case[j] # 현재 스토어의 남은 재고 모두 구매
            buy += stock[store]
            stock[store] = 0

        if max_buy < buy:
            max_buy = buy
            result = [case]
        elif max_buy == buy:
            result.append(case)

    result.sort()
    return result[0]