T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    numbers = list(input())
    count_list = []
    number_list = []
    maxV = 0
    for number in numbers:
        a = numbers.count(number)
        if number not in number_list:
            count_list.append(a)
            number_list.append(number)
            M = max(count_list)
            I = count_list.index(M)

    for number in numbers:
        for i in range(len(count_list)):
            if count_list[i] == M:
                if int(number_list[i]) >=maxV:
                    maxV = int(number_list[i])
    print("#%d"%test_case, maxV, M)



