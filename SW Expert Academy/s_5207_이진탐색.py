for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    n_list = list(map(int, input().split()))
    m_list = list(map(int, input().split()))
    n_list.sort()
    cnt = 0

    for i in m_list:
        # 처음과 끝에는 인덱스 번호를 넣어준다
        left, right = 0, n-1
        target = i
        check = 2
        # 왼쪽 0, 오른쪽은 1로 표현
        while left <= right:
            middle = (left + right) // 2
            if n_list[middle] == target:
                cnt += 1
                break
            # 오른쪽
            elif n_list[middle] > target:
                if check == 1:
                    break
                else:
                    check = 1
                    right = middle - 1
            else:
                if check == 0:
                    break
                else:
                    check = 0
                    left = middle + 1
    print('#{} {}'.format(tc, cnt))