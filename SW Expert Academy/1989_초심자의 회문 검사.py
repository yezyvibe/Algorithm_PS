t = int(input())

for tc in range(1, t+1):
    palindrome = input()
    if palindrome[::] == palindrome[-1::-1]:
        res = 1
    else:
        res = 0

    print('#{} {}'.format(tc, res))