num_list = {}
max_v = 0
result = 0
for _ in range(int(input())):
    number = int(input())
    if num_list.get(number) is None:
        num_list[number] = 1
    else:
        num_list[number] += 1
num_list = sorted(num_list.items())
for key, val in num_list:
    if val > max_v:
        max_v = val
        result = key

print(result)