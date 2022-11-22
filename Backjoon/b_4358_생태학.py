import sys
import math

input = sys.stdin.readline

tree_total_cnt = 0
tree_dict = {}
while True:
    current = input().rstrip()

    if current == "":
        break

    if current in tree_dict:
        tree_dict[current] += 1
    else:
        tree_dict[current] = 1
    tree_total_cnt += 1


answer = []
for key, value in tree_dict.items():
    answer.append([key, format(round((value/tree_total_cnt) * 100, 4), ".4f")])

answer.sort(key=lambda x:x[0])

for current in answer:
    print(" ".join(current))