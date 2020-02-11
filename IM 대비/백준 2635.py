num = int(input())
n1 = num
max_cnt = 0
max_num_list = []

for data in range(num):
    n1 = num
    n2 = data
    cnt = 1
    result = 0
    num_list = []

    while result >= 0:
        num_list.append(n1)
        result = n1 - n2
        n1 = n2
        n2 = result
        cnt += 1

    num_list.append(n1)

    if max_cnt < cnt:
        max_cnt = cnt
        max_num_list = num_list

print(max_cnt)
print(max_num_list)




