n = int(input())

result = 0
for i in range(1,n+1):
    for j in range(i+1):
        result += j
print(result)