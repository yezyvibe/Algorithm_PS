string = input()
bomb = list(input())
stack = []

for i in range(len(string)):
    stack.append(string[i])
    if string[i] == bomb[-1]:
        if stack[-len(bomb):] == bomb:
            for i in range(len(bomb)):
                stack.pop()
if not stack:
    print('FRULA')
else:
    print(''.join(stack))