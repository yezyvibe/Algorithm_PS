from math import factorial


def solution(width, height, diagonals):
    answer = 0
    for x, y in diagonals:
        l_x, l_y = x - 1, y
        left_case_1 = factorial((l_x - 0) + (l_y - 0)) // (factorial(l_x - 0) * factorial(l_y - 0))
        left_case_2 = factorial((width - (l_x + 1)) + (height- (l_y-1))) // (factorial(width - (l_x + 1) ) * factorial(height -(l_y-1)))
        answer += (left_case_1*left_case_2)
        
        r_x, r_y = x, y - 1
        right_case_1 = factorial((r_x - 0) + (r_y - 0)) // (factorial(r_x - 0) * factorial(r_y - 0))
        right_case_2 = factorial((width - (r_x -1)) + (height- (r_y+1))) // (factorial(width - (r_x - 1) ) * factorial(height -(r_y+1)))
        answer += (right_case_1*right_case_2)
    return answer % 10000019