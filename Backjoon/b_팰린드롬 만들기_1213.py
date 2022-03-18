import sys

input = sys.stdin.readline
alpha_dict = {}
for i in list(input().rstrip()):
    if i in alpha_dict:
        alpha_dict[i] += 1
    else:
        alpha_dict[i] = 1

odd_cnt = 0
palindrome = []
tmp = []
for key, value in alpha_dict.items():
    if value % 2 == 1:
        odd_cnt += 1
        if odd_cnt > 1:
            print("I'm Sorry Hansoo")
            break
        else:
            tmp = [key]
            for i in range(value//2):
                palindrome.append(key)
    else:
        for i in range(value//2):
            palindrome.append(key)
else:
    palindrome.sort()
    revese_palindrome = palindrome[::-1]
    answer = palindrome + tmp + revese_palindrome
    print(''.join(answer))
