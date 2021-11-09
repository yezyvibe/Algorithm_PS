# def turn(lst):
#     newArr = ''
#     for i in range(len(lst)):
#         for j in range(len(arr[0]) - 1, -1, -1):
#             newArr += lst[j][i]
#         newArr += ' '
#     return newArr
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     n = int(input())
#     arr = [list(input().split()) for x in range(n)]
#
#     res = [[0] * 3 for y in range(n)]
#     for j in range(3):
#         arr = turn(arr).strip().split()
#         for i in range(n):
#             res[i][j] = arr[i]
#
#     print(f'#{tc}')
#     for i in res:
#         print(' '.join(i))

T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for l in range(N)]
    print('#{}'.format(t))
    for j in range(N):
        for i in range(N):
            print(arr[N-1-i][j], end='')
        print(' ', end='')
        for i in range(N):
            print(arr[N-1-j][N-1-i], end='')
        print(' ', end='')
        for i in range(N):
            print(arr[i][N-1-j], end='')
        print()