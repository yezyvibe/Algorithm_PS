t = int(input())
for tc in range(1, t+1):
    letters = list(input())
    while True:
        a = len(letters)
        for i in range(a-1):
            if letters[i] == letters[i+1]:
                del letters[i:i+2]
                break
        else:
            break
    if letters == []:
        result = 0
    else:
        result = len(letters)

    print('#{} {}'.format(tc, result))