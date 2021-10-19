n, k = map(int, input().split())
tmp_k = k
number = list(map(int, input()))
stack = []

for i in range(n):
    while k and stack and stack[-1] < number[i]:
        stack.pop()
        k -= 1
    stack.append(number[i])
print(''.join(map(str, stack[:n-tmp_k])))