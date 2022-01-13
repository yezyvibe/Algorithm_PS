import sys

input = sys.stdin.readline
for i in range(int(input())):
    o_cnt = 1
    score = 0
    for ox in input():
        if ox == 'O':
            score += o_cnt
            o_cnt += 1
        else:
            o_cnt = 1
    print(score)