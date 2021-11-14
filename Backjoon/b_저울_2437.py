n = int(input())
balances = list(map(int, input().rstrip().split()))
balances.sort()

answer = 1
for i in range(n):
    if answer < balances[i]:
        break
    answer += balances[i]
print(answer)