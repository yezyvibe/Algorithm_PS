import sys
from itertools import combinations as combi


input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0: 
        break

    k, arr = arr[0], arr[1:]

    for c in combi(arr, 6):
        print(" ".join(map(str, c)))
    print()