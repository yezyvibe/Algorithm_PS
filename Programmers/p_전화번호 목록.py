for i in range(len(phone_book)):
    length = len(phone_book[i])
    for j in range(i+1, len(phone_book)):
        tmp = phone_book[i]
        next = phone_book[j][0:length]
        if tmp == next:
            return false
    else:
        return true