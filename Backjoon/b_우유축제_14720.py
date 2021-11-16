n = int(input())
milk_shop = list(map(int, input().split()))
now = 0
answer = 0
for milk in milk_shop:
    if milk == now:
        answer += 1
        now += 1
        if now == 3:
            now = 0
print(answer)