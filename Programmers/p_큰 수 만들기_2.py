def solution(number, k):
    stack = []
    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    return ''.join(stack[:-k]) if k > 0 else ''.join(stack)
        
number  ="1924"
k = 2
print(solution(number, k))