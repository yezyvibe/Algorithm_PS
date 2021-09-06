from itertools import combinations as combi

def solution(orders, course):
    answer = []
    for num in course:
        course_dict = {}
        for order in orders:
            for tmp_course in list(combi(order, num)):
                tmp_course = ''.join(sorted(tmp_course))
                if tmp_course not in course_dict:
                    course_dict[tmp_course] = 1
                else:
                    course_dict[tmp_course] += 1

        max_cnt = 2
        result = []
        for key, value in course_dict.items():
            if max_cnt < value:
                result = [key]
                max_cnt = value
            elif max_cnt == value:
                result.append(key)
        answer += result
    return sorted(answer)

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
print(solution(orders, course))