n = int(input())
arr = sorted((map(int, input().split())))
res = 0
next = 0
for i in arr:
    res += i + next
    next += i
print(res)


