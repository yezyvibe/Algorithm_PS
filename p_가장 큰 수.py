def solution(numbers):
    str_numbers = [str(number) for number in numbers]
    str_numbers = sorted(str_numbers,key= lambda x: x*3, reverse=True)
    answer = ''.join(str_numbers)
    return '0' if int(answer) == 0 else answer


print(solution([3, 30, 34, 5, 9, 0, 0]))
print(solution([0, 0, 0, 0]))