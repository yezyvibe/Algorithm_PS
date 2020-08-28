T = 10
for t_case in range(1, T+1):
    dump = int(input())
    arr = list(map(int, input().split()))
    for i in range(dump):
        arr[arr.index(max(arr))] -= 1
        arr[arr.index(min(arr))] += 1
    result = max(arr) - min(arr)
    print(f'#{t_case} {result}')
