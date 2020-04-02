# for tc in range(1, int(input())+1):
#     n, m = map(int, input().split())
#     n_lst = list(map(int, input().split()))
#
#     for i in range(m):
#         a = n_lst.pop(0)
#         n_lst.append(a)
#
#     res = n_lst[0]
#     print('#{} {}'. format(tc, res))

T = int(input())
for t in range(1, T + 1):
    n, m = map(int, input().split())
    numbers = input().split()
    print(numbers)
    print('#{} {}'.format(t, numbers[m % n]))