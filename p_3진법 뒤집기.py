def change(n):
    if n < 3:
        return str(n)
    q, r = divmod(n, 3)
    return str(change(q)) + str(r)

def solution(n):
    changed_number = change(n)
    return int(changed_number[::-1], 3)