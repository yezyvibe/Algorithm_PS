number = input()
list = []
for i in number[::]:
    list.append(i)
list.sort(reverse=True)

print(''.join(list))

# number = list(input())
# number.sort(reverse=True)
# print(''.join(number))
