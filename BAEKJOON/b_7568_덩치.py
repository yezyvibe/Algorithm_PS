wh_lst =[]
for i in range(int(input())):
    wh_lst.append(list(map(int, input().split())))

for i in wh_lst:
    rank = 1
    for j in wh_lst:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')
