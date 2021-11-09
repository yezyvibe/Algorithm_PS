text = input()
res = []
for i in range(len(text)):
    res.append(text[i:])
res = sorted(res)
print('\n'.join(res))