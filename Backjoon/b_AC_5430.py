import sys
from collections import deque

input = sys.stdin.readline
for _ in range(int(input())):
    function_p = list(input().rstrip())
    n = int(input())
    arr = input()[1:-2].split(",")
    if n > 0:
        arr = deque([int(i) for i in arr])

    reverse_cnt = 0
    for i in function_p:
        if i == 'D':
            if len(arr) == 0 or n == 0:
                print("error")
                break
            if reverse_cnt % 2 == 0:
                arr.popleft()
            else:
                arr.pop()
        elif i == 'R':
            reverse_cnt += 1
    else:
        if reverse_cnt % 2 == 1:
            arr.reverse()
        arr = "[" + ",".join(map(str, arr)) + "]"
        print(arr)