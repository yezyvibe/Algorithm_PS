from itertools import permutations as permu
from collections import deque
from copy import deepcopy


def calculate(op, a, b):
    if op == '*':
        return str(a*b)
    elif op == '-':
        return str(a-b)
    elif op == '+':
        return str(a+b)
    
 
def solution(expression):
    answer = 0
    total_list = deque()
    operator_list = deque()
    tmp = ''
    for i  in expression:
        if i.isdigit():
            tmp += i
        else:
            total_list.append(tmp)
            total_list.append(i)
            operator_list.append(i)
            tmp = ''
    total_list.append(tmp)
    operation_list = list(set(operator_list))


    for item in permu(operation_list, len(operation_list)):
        item = deque(item)
        tmp_list = deepcopy(total_list)
        while item:
            next_list = deque()
            op = item.popleft()
            while tmp_list:
                a = tmp_list.popleft()
                if a.isdigit():
                    next_list.append(a)
                else:
                    if op == a:
                        c = tmp_list.popleft()
                        b = next_list.pop()
                        next_list.append(calculate(a, int(b), int(c)))
                    else:
                        next_list.append(a)
            tmp_list = deepcopy(next_list)
        answer = max(answer, abs(int(next_list[0])))
    return answer
expression = "100-200*300-500+20"
print(solution(expression))

