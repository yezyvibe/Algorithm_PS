import sys

input = sys.stdin.readline
join_list = []
for i in range(int(input())):
    age, name = input().split()
    join_list.append((age, i, name))
join_list.sort(key=lambda x: (int(x[0]), x[1]))
for people in join_list:
    print(people[0] + ' ' + people[2])