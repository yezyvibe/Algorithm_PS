import math 

def check_referral(member_map, seller_name):
    if member_map[seller_name][0] == "-":
        return True
    return False


def solution(enroll, referral, seller, amount):
    member_map = dict()
    for i in range(len(enroll)):
        member_map[enroll[i]] = [referral[i], 0]
    
    for i in range(len(seller)):
        seller_name = seller[i]
        profit = amount[i] * 100
        ten_percent = math.floor(profit * 0.1)

        while True:
            if ten_percent >= 1:
                profit -= ten_percent
                if (check_referral(member_map, seller_name)):
                    member_map[seller_name][1] += profit
                    break
                else:
                    member_map[seller_name][1] += profit
                    seller_name = member_map[seller_name][0]
                    profit = ten_percent
                    ten_percent = math.floor(profit * 0.1)
            else:
                member_map[seller_name][1] += profit
                break

    return [member_map[name][1] for name in enroll]
                




enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
print(solution(enroll, referral, seller, amount))