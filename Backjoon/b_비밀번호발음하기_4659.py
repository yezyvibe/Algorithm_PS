import sys

input = sys.stdin.readline

while True:
    chk = 0
    password = input().rstrip()
    if password == 'end':
        break
    # 1단계
    for i in 'aeiou':
        if i in password:
            break
    else:
        print(f'<{password}> is not acceptable.')
        continue
    # 2단계
    consonant_cnt, vowel_cnt = 0, 0
    for i in password:
        if i in 'aeiou':
            vowel_cnt += 1
            consonant_cnt = 0
        else:
            consonant_cnt += 1
            vowel_cnt = 0
        if vowel_cnt >= 3 or consonant_cnt >= 3:
            print(f'<{password}> is not acceptable.')
            chk = 1
            break
    if chk:
        continue
    # 3단계
    s = []
    for i in password:
        if not s:
            s.append(i)
        else:
            if s[-1] == i:
                if i != 'e' and i != 'o':
                    print(f'<{password}> is not acceptable.')
                    break
            else:
                s.append(i)
    else:
        print(f'<{password}> is acceptable.')
    