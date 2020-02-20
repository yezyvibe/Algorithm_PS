import copy
t = int(input())
num = [1,2,3,4,5,6,7,8,9]

for tc in range(1, t+1):
    arr =[list(map(int,input().split())) for l in range(9)]
    result = 1

    arr2=copy.deepcopy(arr)
    for i in range(9):
        i_row = arr2[i]
        i_row.sort()
        if i_row == num:
            pass
        else:
            result = 0
            break

    if result != 0:
        for j in range(9):
            new = []
            for k in range(9):
                i_column = arr[k][j]
                new.append(i_column)
            new.sort()
            if new == num:
                pass
            else:
                result = 0
                break

    if result != 0:
        for i in range(0,9,3):
            for j in range(0,9,3):
                s = []
                for k in range(3):
                    for m in range(3):
                        a = arr[i+k][j+m]
                        s.append(a)
                s.sort()
                if s == num:
                    pass
                else:
                    result = 0
                    break
    print('#{} {}'.format(tc, result))