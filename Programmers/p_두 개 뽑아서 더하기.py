from itertools import combinations as combi

def solution(numbers):
    answer = set()
    n_lst = list(combi(numbers, 2))
    for n in n_lst:
        a, b = n
        answer.add(a + b)
    answer = sorted(list(answer))
    return answer