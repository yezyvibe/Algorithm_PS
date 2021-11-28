import sys

input = sys.stdin.readline

for i in range(3):
    yut = list(input())
    zero_cnt = yut.count('0')
    if zero_cnt == 1:
        print('A')
    elif zero_cnt == 2:
        print('B')
    elif zero_cnt == 3:
        print('C')
    elif zero_cnt  == 4:
        print('D')
    else:
        print('E')