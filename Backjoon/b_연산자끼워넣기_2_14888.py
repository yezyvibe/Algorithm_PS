import sys
from itertools import permutations as permu


def caculate(operations, numbers):
    start = numbers[0]

    for i in range(1, len(numbers)):
        next = numbers[i]
        op = operations[i-1]
        
        if op == '+':
            start += next
        elif op == '-':
            start -= next
        elif op == '*':
            start *= next
        elif op == '/':
            if start < 0 and next > 0:
                start = -((-start) // next)
            elif start > 0 and next < 0:
                start = -((start) // -next)
            else:
                start = start // next
    return start


input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
operations = list(map(int, input().split()))


# 완전 탐색 가능한 범위
op = []
tmp = ['+', '-', '*', '/']
for i in range(4):
    for j in range(operations[i]):
        op.append(tmp[i])

max_value = -1000000000
min_value = 1000000000
for k in permu(op, n-1):
    candidate = list(k)
    result = caculate(candidate, arr)
    max_value = max(max_value, result)
    min_value = min(min_value, result)

print(max_value)
print(min_value)
