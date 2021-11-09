n = 26

a = n//10 #십의자리
b = n%10 #일의자리
c = (a + b) % 10  #일의자리
d = b*10 + c
cnt = 1

while n != d :
    a = d // 10
    b = d % 10
    c = (a + b) % 10
    d = b * 10 + c
    cnt += 1


print(d)
print(cnt)

