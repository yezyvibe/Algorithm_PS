string = input()
result = set()

for i in range(len(string)):
    for j in range(i+1, len(string)+1):
        result.add(string[i:j])
answer = len(result)
print(answer)
