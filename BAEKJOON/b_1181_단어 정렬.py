word_lst = []
for i in range(int(input())):
    word = input()
    if (len(word), word) not in word_lst:
        word_lst.append((len(word), word))
word_lst = sorted(word_lst, key=lambda x: (x[0], x[1]))

for w in word_lst:
    print(w[1])


# import sys
#
# input = sys.stdin.readline
# w = set()
# for i in range(int(input())):
#     w.add(input().rstrip())
# w_list = list(w)
# w_list.sort()
# w_list.sort(key=lambda x: len(x))
# print("\n".join(w_list))

