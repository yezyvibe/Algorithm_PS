import sys

input = sys.stdin.readline
n = int(input())
chk = []

for _ in range(n):
    options = input().rstrip().split(' ')
    end_chk = 0
    # print(options)

    for k in range(len(options)): # 단어의 첫 글자가 단축키가 되는지 확인
        if options[k][0].upper() not in chk:
            chk.append(options[k][0].upper())
            options[k] = '['+options[k][0]+']'+options[k][1:]
            res = ' '.join(options)
            print(res)
            break
    else:
        for i in range(len(options)):
            for j in range(1, len(options[i])): # 모든 첫 글자 단축키 지정된 경우, 왼쪽부터 차례대로 확인
                tmp = options[i][j].upper()
                if tmp not in chk:
                    # print(tmp, 'tmp')
                    chk.append(tmp)
                    options[i] = options[i][:j]+'['+options[i][j]+']'+options[i][j+1:]
                    res = ' '.join(options)
                    print(res)
                    end_chk = 1
                    break
            if end_chk:
                break
        else:
            res = ' '.join(options)  # 아무것도 단축키 지정하지 못하는 경우 그냥 출력
            print(res)