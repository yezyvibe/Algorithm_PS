document = input()
word = input()
idx = 0
answer = 0
while idx < len(document):
    if document[idx:idx+len(word)] == word:
        idx += len(word)
        answer += 1
    else:
        idx += 1
print(answer)