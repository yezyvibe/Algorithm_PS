T = int(input())
shapes = ['S', 'D', 'H', 'C']


for tc in range(1, T+1):
    word = input()
    word_cnt = []

    S_cnt = 0
    D_cnt = 0
    H_cnt = 0
    C_cnt = 0

    for i in range(0,len(word),3):
        word_cnt.append(word[i:i+3])


    for n in word_cnt:
        print(n)
        if n.startswith("S"):
            S_cnt += 1
        elif n[0] == 'D':
            D_cnt += 1
        elif n[0] == 'H':
            H_cnt += 1
        elif n[0] == 'C':
            C_cnt += 1

    word_cnt2 = word_cnt
    if len(word_cnt2) != len(set(word_cnt)):
        print('#{} ERROR' .format(tc))
    else:
        print('#{} {} {} {} {}' .format(tc, 13-S_cnt, 13-D_cnt, 13-H_cnt, 13-C_cnt))


