def solution(s):
    small_letters = []
    capital_letters = []
    for i in s:
        if i.isupper():
            capital_letters.append(i)
        else:
            small_letters.append(i)
    small_letters.sort(reverse=True)
    capital_letters.sort(reverse=True)
    small_letters.extend(capital_letters)
    return(''.join(small_letters))