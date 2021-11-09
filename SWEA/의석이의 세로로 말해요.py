T = int(input())
for tc in range(1, T+1):
    word = [list(input()) for n in range(5)]

    result = ''
    for i in range(len(word)):
        for j in range(len(word)):
            if word[j][i] =='':
                pass
            else :
                result += word[j][i]




    print(result)



