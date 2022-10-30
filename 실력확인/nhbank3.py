def solution(n, records, cart, k):
    result = [[0]*(len(cart)+1) for _ in range(n+1)]
    # 각 물건을 구매한 빈도수 저장
    for r in records:
        r = r.split(" ")
        for j in range(1, len(r)):
            cur = int(r[j])
            if cur in cart:
                continue
            result[cur][-1] += 1
    print(result)

    # 같이 물건을 구매한 빈도수
    for r in records:
        r = r.split(" ")

        for j in range(1, len(r)):
            cur = int(r[j])
            for i in range(len(cart)):
                if cart[i] == cur:
                    for k in r[1:]:
                        if k != cur:
                            result[int(k)][i] += 1          

    print(result)

    # 확률 구하기
    answer = [0] * (n+1)
    for i in range(len(answer)):
        tmp = 0
        for j in range(1, len(result[i])):
            tmp += result[i][j]