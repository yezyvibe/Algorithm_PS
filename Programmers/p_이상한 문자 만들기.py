def solution(s):
    answer = ''
    words = list(s.split(' '))
    for word in words:
        word = list(word)
        for i in range(len(word)):
            if i % 2 == 0:
                word[i] = word[i].upper()
            else:
                word[i] = word[i].lower()
            answer += word[i]
        answer += ' '
    return answer[0:-1]



sum(map(int,str(number)))