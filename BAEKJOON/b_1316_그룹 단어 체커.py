cnt = 0
for i in range(int(input())):
    word = input()
    word_lst = [word[0]]
    for k in range(1, len(word)):
        if word[k] != word[k - 1]:
            word_lst.append(word[k])
    word_set = set(word_lst)

    if len(word_lst) == len(word_set):
        cnt += 1

print(cnt)
