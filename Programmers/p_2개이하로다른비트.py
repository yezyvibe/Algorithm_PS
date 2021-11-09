def solution(numbers):
    answer = []
    for num in numbers:
        num_bit = bin(num)[2:]
        while True:
            num += 1
            next_num_bit = bin(num)[2:]
            while len(num_bit) < len(next_num_bit):
                num_bit = '0' + num_bit
            cnt = 0
            for i in range(len(num_bit)):
                if num_bit[i] != next_num_bit[i]:
                    cnt += 1
                    if cnt > 2:
                        break
            else:
                answer.append(num)
                break

    return answer
numbers = [2, 7]
print(solution(numbers))