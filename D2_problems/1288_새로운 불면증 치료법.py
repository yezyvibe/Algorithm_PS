T = int(input())
for t in range(1, T+1):
    set_list = set()
    N = int(input())
    count = 0
    while len(set_list) < 10:
        count += 1
        temp = N * count
        temp = set(map(int, list(str(temp))))
        set_list |= temp
        print(set_list)
    # print('#{} {}'.format(t, N*count))