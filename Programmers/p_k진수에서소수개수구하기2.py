def check_prime_number(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            # 나누어 떨어지면 소수 아님
            return False
    return True
    
def solution(n, k):
    decimal = ""
    while n >= k:
        q, r = divmod(n, k)
        decimal = str(r) + decimal
        n = q
    
    if n != 0:
        decimal = str(n) + decimal

    decimal = decimal.split("0")
    answer = 0
    for i in range(len(decimal)):
        cur_num = decimal[i]
        if cur_num == '1' or cur_num == '':
            continue
        if check_prime_number(int(decimal[i])):
            answer += 1
    return answer

print(solution(110011, 10))