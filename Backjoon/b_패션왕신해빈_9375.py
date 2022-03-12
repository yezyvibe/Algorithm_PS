import sys


input = sys.stdin.readline

for i in range(int(input())):
    fashion_dict = {}   
    for k in range(int(input())):
        name, kind = map(str, input().split())
        if kind in fashion_dict:
            fashion_dict[kind].append(name)
        else:
            fashion_dict[kind] = [name]
    answer = 1
    for key, value in fashion_dict.items():
        answer *= (len(value)+1)
    print(answer-1)