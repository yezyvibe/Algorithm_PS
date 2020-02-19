t = int(input())
a_lst = ['{', '(']
a_res = []
b_lst = ['}', ')']
b_res = []
total = ['{', '}', '(', ')']


for tc in range(1, t+1):
    words = list(input())
    for word in words:
        if word in a_lst:
            a_res.append(word)

    for word in words[::-1]:
        if word in b_lst:
            b_res.append(word)

    result = ''
    if len(a_res) != len(b_res):
        result = 0
    else:
        for i in a_res:
            print(a_res.index[i])
            b_res.remove(total[a_res.index(i)+1])
            print(b_res)
