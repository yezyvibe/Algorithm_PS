import sys

input = sys.stdin.readline
word_list = []
max_len = 0
answer = ''
for i in range(5):
    word = input().rstrip()
    word_list.append(word)
    max_len = max(max_len, len(word))
for i in range(max_len+1):
    for j in range(len(word_list)):
        try: 
            answer += word_list[j][i]
        except:
            continue
print(answer)