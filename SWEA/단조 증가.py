T = int(input())

for tc in range(1,T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    mul_list = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
                mul = numbers[i]*numbers[j]
                mul_list.append(mul)
    result = []
    for num in mul_list:
        num_str = str(num)
        for n in range(len(num_str)-1):
            if num_str[n+1] >= num_str[n]:
                result.append(num_str)

    res = max(result)
    if result == []:
        res = -1

    print(f'#{tc} {res}')









