from itertools import permutations as permu
def decimal(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    permu_res = set()
    for i in range(1, len(numbers)+1):
        for k in set(permu(numbers, i)):
            tmp = int(''.join(map(str, k)))
            permu_res.add(tmp)
    for num in permu_res:
        if decimal(num):
            answer += 1
    return answer
numbers = "17"
print(solution(numbers))