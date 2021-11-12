kind_of_money = [500, 100, 50, 10, 5, 1]
payment = 1000 - int(input())

idx = 0
answer = 0
while payment != 0:
    if payment >= kind_of_money[idx]:
        q, r = divmod(payment, kind_of_money[idx])
        payment = r
        answer += q
    idx += 1
print(answer)