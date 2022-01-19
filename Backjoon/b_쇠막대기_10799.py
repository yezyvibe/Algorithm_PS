bracket = list(input())
stack = []
answer = 0
for i in range(len(bracket)):
    if bracket[i] == "(":
        stack.append("(")
    else:
        if bracket[i-1] == "(":
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1
print(answer)
