T = 10
for test_case in range(1, T + 1):
    jomang = 0
    building = int(input())
    datas = list(map(int, input().split()))

    for i in range(2, len(datas)-2):
        jo = datas[i]- max(datas[i-2],datas[i-1],datas[i+1],datas[i+2])
        if jo > 0:
            jomang = jomang + jo
    print( f'#{test_case} {jomang}')
