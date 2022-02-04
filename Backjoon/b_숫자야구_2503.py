from itertools import permutations as permu
import sys

input = sys.stdin.readline
n = int(input())
answer = list(permu(['1','2','3','4','5','6','7','8','9'], 3))
for _ in range(n):
    question, s, b = map(int, input().split())
    question = list(str(question))
    remove_cnt = 0
    for i in range(len(answer)):
        strike = ball = 0
        i -= remove_cnt
        for j in range(3):
            if question[j] == answer[i][j]:
                strike += 1
            elif question[j] in answer[i]:
                ball += 1
        if strike != s or ball != b:
            answer.remove(answer[i])
            remove_cnt += 1
print(len(answer))