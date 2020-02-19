t = int(input())

for tc in range(1,t+1):
    pattern = input()
    for i in range(1,11):
        if pattern[:i] == pattern[i:i+i]:
            res = len(pattern[:i])
            break
    print('#{} {}'.format(tc, res))