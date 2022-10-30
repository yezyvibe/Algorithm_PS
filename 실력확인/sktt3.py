def solution(s, word_dict):
    result = []

    def dfs(origin, cur_word, cnt):
        nonlocal result

        if len(cur_word) > len(origin):
            return

        if cur_word == origin:
            result.append(cnt)
            return 

        for i in range(len(word_dict)):
            if word_dict[i][0] == cur_word[-1]:
                dfs(origin, cur_word + word_dict[i][1:], cnt + 1)

    #첫 단어 찾기
    idx = 0
    start_words = []
    for i in range(len(word_dict)):
        cur = word_dict[i]
        if s[idx:idx+len(cur)] == cur:
            start_words.append(cur)
    for i in range(len(start_words)):
        word_dict.remove(start_words[i])

    for start in start_words:
        dfs(s, start, 1)

    return max(result)