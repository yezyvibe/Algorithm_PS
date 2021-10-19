n = int(input())
info = input()
cup_holder = ["*",]
chk = 0
for i in info:
    if i == "S":
        cup_holder.append("*")
    elif i == "L" and not chk:
        chk = 1
        continue
    elif i == "L" and chk:
        chk = 0
        cup_holder.append("*")
print(min(cup_holder.count("*"), n))
