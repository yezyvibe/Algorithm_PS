# import sys

# input = sys.stdin.readline
# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# start, end = max(arr), sum(arr)

# while start <= end:
#     mid = (start + end) // 2
#     count = 0
#     tmp = 0
#     for number in arr:
#         if tmp + number > mid:
#             count += 1
#             tmp = 0
#         tmp += number
#     if tmp:
#         count += 1
#     if count <= m:
#         end = mid - 1
#     else:
#         start = mid + 1
# print(start)



import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))

start, end = max(arr), sum(arr)     ### 범위 조심!!!
while start <= end:
    result = []
    mid = (start + end) // 2
    tmp = 0 
    for i in arr:        
        if tmp + i > mid:
            result.append(tmp)
            tmp = i
        else:
            tmp += i
        
    if len(result) >= m:
        start = mid + 1
    elif len(result) < m:
        end = mid - 1
print(start)