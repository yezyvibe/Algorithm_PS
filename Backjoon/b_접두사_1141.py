import sys

input = sys.stdin.readline
word_list = []
for i in range(int(input())):
    word_list.append(input().rstrip())
word_list.sort()

answer = 0
for i in range(len(word_list)):
    for j in range(i+1, len(word_list)):
        if word_list[i] == word_list[j][:len(word_list[i])]:
            break
    else:
        answer += 1

print(answer)
