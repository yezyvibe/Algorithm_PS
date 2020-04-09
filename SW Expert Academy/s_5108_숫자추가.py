for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    n_list = list(map(int, input().split()))

    for i in range(M): # 인덱스와 숫자 정보
        index, number = map(int, input().split()) # 인풋 완료
        n_list.insert(index, number)

    print(f'#{tc} {n_list[L]}')