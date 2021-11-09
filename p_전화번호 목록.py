def solution(phone_book):
    phone_book = sorted(phone_book)
    for i in range(1, len(phone_book)):
        num_len = len(phone_book[i-1])
        if phone_book[i-1] == phone_book[i][:num_len]:
            return False
    else:
        return True



phone_book = ["12","123","1235","567","88"]
print(solution(phone_book))