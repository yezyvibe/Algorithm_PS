import math 


def solution(enroll, referral, seller, amount):
    # 자신을 영입한 판매원 이름을 딕셔너리로 저장, 이때 본인 수익도 함께 저장
    # 그 다음 seller, amount 배열을 돌면서 수익 배분
    # 타고 타고 올라갔을 때 판매원이 없으면 수입 배분 끝

    dict = {}
    for i in range(len(enroll)):
        dict[enroll[i]] = [referral[i], 0]
    
    for i in range(len(seller)):
        cur_seller, cur_amount = seller[i], amount[i]
        current = int(cur_amount * 100)
        while True:
            for_referrel = int(current * 0.1)
            if for_referrel == 0:
                dict[cur_seller][1] += current
                break
            for_seller = current - for_referrel
            dict[cur_seller][1] += for_seller
            next = dict[cur_seller][0]
            if next != '-':
                cur_seller = next
                current = for_referrel
            else:
                break
    
    result = []
    for member in enroll:
        result.append(dict[member][1])
    return result
    
print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))