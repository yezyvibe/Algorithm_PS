def solution(s):
    num_dict = {'zero': 0, 'one': 1, 'two':2, 'three':3, 'four': 4,
                'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    
    answer = []
    stack = []
    for i in s:
        if i.isdigit():
            answer.append(i)
        else:
            stack.append(i)
            tmp = ''.join(stack)
            if tmp in num_dict:
                answer.append(str(num_dict[tmp]))
                stack = []
    return int(''.join(answer))




# num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

# def solution(s):
#     answer = s
#     for key, value in num_dic.items():
#         answer = answer.replace(key, value)
#     return int(answer)