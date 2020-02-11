di = [-1,0,1,0]
dj = [0,1,0,-1]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    res = 0

    print(arr)

    print('#{} {}'.format(tc, res))