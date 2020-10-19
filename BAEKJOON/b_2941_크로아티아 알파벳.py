alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

idx = 0
cnt = 0
while True:
    if word[idx:idx + 2] in alpha:
        idx += 2
        cnt += 1
    elif word[idx:idx + 3] in alpha:
        idx += 3
        cnt += 1
    else:
        idx += 1
        cnt += 1
    if len(word) == idx:
        break
print(cnt)
#
# word = input()
# for t in alpha: word = word.replace(t, '*')
# print(len(word))
