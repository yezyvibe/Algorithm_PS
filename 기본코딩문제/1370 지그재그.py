n = int(input())

for i in range(n):
    a = ' '*(n-i-1) + '*' +' '*i + ' '*i + '*'
    print(a)
for i in range(n):
    b = ' '*i + '*' + ' ' * (n - i - 1) + ' ' * (n - i - 1) + '*'
    print(b)
