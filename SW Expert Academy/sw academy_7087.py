t = int(input())
for tc in range(1,t+1):
    arr = [0 for k in range(26)]
    n = int(input())
    for i in range(n):
        word = input()
        word_str = word[0]
        idx = ord(word_str) - ord('A')
        arr[idx] = 1

    cnt = 0
    for j in arr:
        if j == 1:
            cnt += 1
        else:
            break
    print('#{} {}'.format(tc, cnt))


