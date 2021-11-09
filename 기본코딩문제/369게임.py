num_list = []
result = 0

for i in range(1,100):
    a = str(i)
    if i <= 10:
       if int(a) % 3 == 0:
           result = '짝'
       else:
           result = i

    else:
        if int(a) % 10 == 0:
            result = i
            if int(a) % 30 == 0:
                result = '짝'
        elif int(a[0]) % 3 == 0:
            result = '짝'
            if int(a[1]) % 3 == 0:
                result ='짝짝'
        elif int(a[1]) % 3 == 0:
            result = '짝'
        else:
            result = i
    num_list.append(result)

print(num_list)



