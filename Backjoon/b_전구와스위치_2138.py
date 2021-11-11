import sys

def convert(k, arr):
    if arr[k]:
        arr[k] = 0
    else:
        arr[k] = 1

# 첫 번째 전구 상태 바꾸고 시작
def firstSwitch(arr):
    count = 1
    convert(0, arr)
    convert(1, arr)
    for i in range(1, n):
        if arr[i-1] != arr_b[i-1]:
            count += 1
            convert(i-1, arr)
            convert(i, arr)
            if i != n-1:
                convert(i+1, arr)
    if arr == arr_b:
        return count
    return -1

# 첫 번째 전구 상태 바꾸지 않고 시작
def firstNoSwitch(arr):
    count = 0
    for i in range(1, n):
        if arr[i-1] != arr_b[i-1]:
            count += 1
            convert(i-1, arr)
            convert(i, arr)
            if i != n-1:
                convert(i+1, arr)
    if arr == arr_b:
        return count
    return -1


input = sys.stdin.readline
n = int(input())
arr_a = list(map(int, input().rstrip()))
arr_b = list(map(int, input().rstrip()))
count = 0

res1 = firstSwitch(arr_a[:])
res2 = firstNoSwitch(arr_a[:])

if res1 == -1 and res2 == -1:
    print(-1)
elif res1 == -1:
    print(res2)
elif res2 == -1:
    print(res1)
else:
    print(min(res1, res2))

