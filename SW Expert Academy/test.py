T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [[]*2 for i in range(N)]
    print(arr)
    # arr[0].append(1)
    # for i in range(N-1):
    #     for j in range(i+2):
    #         if j == 0 or j == len(arr[i]):
    #             arr[i+1].append(arr[0][0])
    #         else:
    #             arr[i+1].append(arr[i][j-1]+arr[i][j])
    # print('#{}'.format(t))
    # for idx, i in enumerate(arr):
    #     for j in range(len(i)):
    #         print(i[j], end=" ")
    #     print()