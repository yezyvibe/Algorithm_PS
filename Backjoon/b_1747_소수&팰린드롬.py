# 10시 20 - 40분까지 (20분 소요)
n = int(input())
while True:
    if n == 1:  # 예외처리
        print(2)
        break
    n_lst = list(str(n))
    n_reverse = list(reversed(n_lst))
    if n_lst == n_reverse:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            print(n)
            break
    n += 1
