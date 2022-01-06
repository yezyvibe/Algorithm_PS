import sys

def binary_search(number):
    start, end = 0, len(note_1) - 1
    while start <= end:
        mid = (start + end) // 2
        if note_1[mid] > number:
            end = mid - 1
        elif note_1[mid] < number:
            start = mid + 1
        elif note_1[mid] == number:
            return True
    return False


input = sys.stdin.readline
t = int(input())

for i in range(t):
    n = int(input())
    note_1 = list(map(int, input().split()))
    note_1.sort()

    m = int(input())
    note_2 = list(map(int, input().split()))

    for number in note_2:
        if binary_search(number):
            print(1)
        else:
            print(0)


