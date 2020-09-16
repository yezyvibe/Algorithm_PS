def solution(n):
    answer = []
    for i in range(n + 1):
        answer.append([0] * i)
    cnt = 1
    k = 0
    j = 1

    for idx in range(1, n + 1):
        print(idx)
        if idx % 3 == 1:
            while j < n + 1:
                if not answer[j][k]:
                    answer[j][k] = cnt
                    cnt += 1
                j += 1
            j -= 1
            print(answer, j, k)

        elif idx % 3 == 2:
            while k < n:
                if not answer[j - 1][k]:
                    answer[j - 1][k] = cnt
                    cnt += 1
                k += 1
            print(answer, j, k)

        elif idx % 3 == 0:
            while j > 1 and k > 0:
                if not answer[j - 1][k - 1]:
                    answer[j - 1][k - 1] = cnt
                    cnt += 1
                j -= 1
                k -= 1
            j += 1
            k += 1

            print(answer, j, k)

    # print(answer)
    return answer