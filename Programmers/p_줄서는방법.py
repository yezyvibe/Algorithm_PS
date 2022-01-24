def solution(n, k):
    def factorial(n):
        total = 1
        for i in range(1, n+1):
            total *= i
        return total
    
    answer = []
    numbers = [i for i in range(1, n+1)]
    
    while n > 0:
        # n은 채워야 하는 숫자 개수, step은 각 단계별 채울 숫자(맨 첫번째부터 시작한다)
        # factorial(n) // n은 각 숫자별 총 개수
        # 앞자리 하나씩 결정해 나가기
        step, k = divmod(k, factorial(n) // n)
        if k == 0:
            answer.append(numbers.pop(step-1))
        else:
            answer.append(numbers.pop(step))
        n -= 1
    return answer

print(solution(3, 5))