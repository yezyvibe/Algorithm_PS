import sys


input = sys.stdin.readline
numbers = input().rstrip()
numbers = numbers.split('-')

answer = 0
for i in range(len(numbers)):
    total = sum(map(int, numbers[i].split("+")))
    
    if i == 0:
        answer += total
    else:
        answer -= total    
    
print(answer)
