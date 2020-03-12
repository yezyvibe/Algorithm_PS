for t in range(1, int(input())+1):
    arr = list(input())
    tmp = []
    res = [13, 13, 13, 13]
    for i in range(0, len(arr), 3):
        if arr[i:i+3] in tmp:
            res = 'ERROR'
            break
        else:
            tmp.append(arr[i:i+3])

        if arr[i] == 'S':
            res[0] -= 1
        elif arr[i] == 'D':
            res[1] -= 1
        elif arr[i] == 'H':
            res[2] -= 1
        else:
            res[3] -= 1
    print('#{}'.format(t), end=' ')
    if res == 'ERROR':
        print('ERROR')
    else:
        print(' '.join(map(str, res)))