import sys

input = sys.stdin.readline
for i in range(int(input())):
    sentence = input().rstrip().split(' ')
    for j in range(len(sentence)):
        word = sentence[j]
        sentence[j] = word[::-1]
    print(' '.join(sentence))
