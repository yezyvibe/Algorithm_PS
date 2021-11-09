def solution(numbers, hand):
    left, right = [1, 4, 7], [3, 6, 9]
    answer = ''
    current_left = 10
    current_right = 12
    for num in numbers:
        if num in left:
            answer += 'L'
            current_left = num
        elif num in right:
            answer += 'R'
            current_right = num
        else:
            if num == 0:
                num = 11
            abs_l = abs(num-current_left)
            abs_r = abs(num-current_right)
            if sum(divmod(abs_l, 3)) > sum(divmod(abs_r, 3)):
                answer += 'R'
                current_right = num
            elif sum(divmod(abs_l, 3)) < sum(divmod(abs_r, 3)):
                answer += 'L'
                current_left = num
            else:
                if hand == 'right':
                    answer += 'R'
                    current_right = num
                else:
                    answer += 'L'
                    current_left = num
    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'
print(solution(numbers, hand))