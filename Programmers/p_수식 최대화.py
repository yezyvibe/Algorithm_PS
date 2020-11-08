from itertools import permutations as permu
from collections import deque

def operation(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    elif op == '-':
        return str(int(num1) - int(num2))
    elif op == '*':
        return str(int(num1) * int(num2))

def calculate(ex, op):
    print(op)
    ex = deque(ex)
    stack = []
    for o in op:
        while True:
            if len(ex) == 0:
                break
            tmp = ex.popleft()
            if tmp == o: # 우선순위에 해당하는 연산자가 나온 경우
                # stack에 먼저 저장해둔 숫자 빼고, ex에서 그 다음 숫자 빼서 연산하기
                stack.append(operation(stack.pop(), ex.popleft(), o)) #계산한 결과 다시 stack에 담기
            else:
                stack.append(tmp)
        result = stack
        ex = deque(stack)
        stack = []
    return result


def solution(expression):
    expression += '#'
    ex = []
    tmp = ''
    for e in expression:
        if e.isdigit():
            tmp += e
        else:
            if e == '#':
                ex.append(tmp)
            else:
                ex.append(tmp)
                ex.append(e)
                tmp = ''
    print(ex)

    answer = 0
    for op in permu(['*', '-', '+'], 3):
        answer = max(answer, abs(int(calculate(ex, op)[0])))
    print(answer)
    return answer

expressions = "100-200*300-500+20"
solution(expressions)