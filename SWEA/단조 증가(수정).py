T = int(input())
for tc in range(1,T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = []

    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
                mul = numbers[i]*numbers[j]
                num_str = str(mul)
                for n in range(len(num_str)-1):
                    if num_str[n+1] >= num_str[n]:
                        pass
                    else:
                        break
                else:
                    result.append(mul)

    if result == []:
        res = -1
    else :
        res = max(result)
    print('#{} {}'.format(tc, res))