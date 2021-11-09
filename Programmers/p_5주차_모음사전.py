def solution(word):
    result = []
    def dictionary(s):
        if len(s) == 6:
            return
        else:
            result.append(s)

        for i in ['A', 'E', 'I', 'O', 'U']:
            dictionary(s+i)
        

    for i in ['A', 'E', 'I', 'O', 'U']:
        dictionary(i)
    return result.index(word)

print(solution('AAAAE'))