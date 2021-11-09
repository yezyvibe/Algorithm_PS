import sys

input = sys.stdin.readline
arr = []

for i in range(int(input())):
    n = int(input())
    arr.append(n)

arr = sorted(arr)

for i in arr:
    print(i)
