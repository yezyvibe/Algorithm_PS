word = input()
if len(word) % 2 == 0:
    if word[:len(word)//2] == word[len(word)//2:][::-1]:
        print(1)
    else:
        print(0)
else:
    if word[:len(word)//2] == word[len(word)//2+1:][::-1]:
        print(1)
    else:
        print(0)