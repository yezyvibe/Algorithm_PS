import sys

target_num = 100
dwarfs = []
for _ in range(9):
    height = sys.stdin.readline()
    dwarfs.append(int(height))
dwarfs = sorted(dwarfs)
for i in range(9):
    for j in range(i+1, 9):
        tmp = dwarfs[i] + dwarfs[j]
        if sum(dwarfs)-int(tmp) == target_num:
            for k in range(9):
                if k != i and k != j:
                    print(dwarfs[k])
            sys.exit()