def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))

numbers = [0,0,0,0,0]
print(solution(numbers))