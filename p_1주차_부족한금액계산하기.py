def solution(price, money, count):
    required_money = 0
    current_count = 1
    while current_count < count+1:
        required_money += (price*current_count) 
        current_count += 1
    return abs(required_money - money) if required_money > money else 0


print(solution(3, 20, 4))