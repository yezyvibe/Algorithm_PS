import sys

input = sys.stdin.readline
books = {}
for i in range(int(input())):
    name = input().rstrip()
    if name in books:
        books[name] += 1
    else:
        books[name] = 1

answer = []
max_cnt= 0
for key, value in books.items():
    if value > max_cnt:
        answer = [key]
        max_cnt = value
    elif value == max_cnt:
        answer.append(key)
answer.sort()
print(answer[0])