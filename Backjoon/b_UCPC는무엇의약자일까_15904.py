s = input()
target = ['U', 'C', 'P', 'C']
idx = 0
chk = 0

for i in range(4):
    idx = s.find(target[i])
    if idx == -1:
        print("I hate UCPC")
        break
    s = s[idx+1:]
else:
    print("I love UCPC")