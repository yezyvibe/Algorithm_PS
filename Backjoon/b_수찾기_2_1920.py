import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
chk_arr = list(map(int, input().split()))
arr.sort()

for i in range(m):
    
    cur = chk_arr[i]
    start, end = 0, n - 1 # 인덱스

    while start <= end:
        mid = (start + end) // 2

        if cur == arr[mid]:
            print(1)
            break

        elif cur > arr[mid]:
            start = mid + 1

        elif cur < arr[mid]:
            end = mid - 1
    else:
        print(0)
