import sys 

def binary_search(x):
    start, end = 0, len(lis) - 1
    while start < end:
        mid = (start + end) // 2
        if lis[mid] < x:
            start = mid + 1
        else:
            end = mid
    return end

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
lis = []

for number in arr:
    if not lis:
        lis.append(number)
        continue
    if lis[-1] < number:
        lis.append(number)
    else:
        lis[binary_search(number)] = number
        
print(n - len(lis))