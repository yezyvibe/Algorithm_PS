import sys

input = sys.stdin.readline
n = int(input())
word = [input().rstrip() for _ in range(n)]
dict = {}
for i in range(n):
    k = 0
    for j in word[i][::-1]:
        if j not in dict:
            dict[j] = 10 ** k
        else:
            dict[j] += 10 ** k
        k += 1

word_list = []
for key, value in dict.items():
    word_list.append([value, key])
word_list.sort(key=lambda x:-x[0])

number = 9
for value, key in word_list:
    dict[key] = str(number)
    number -= 1

answer = 0
for i in range(n):
    tmp = ''
    for j in word[i]:
        tmp += dict[j]
    answer += int(tmp)

print(answer)