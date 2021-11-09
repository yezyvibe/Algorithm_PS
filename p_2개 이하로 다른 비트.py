def solution(numbers):
    answer = []
    for num in  numbers:
        if num % 2 == 0:
            res = bin(num)[2:-1] + "1"
            answer.append(int(res, 2))
        else:
            tmp = "0"+ bin(num)[2:] 
            idx = tmp.rfind("0")
            
            res = tmp[:idx] + '10' + tmp[idx+2:]
            print(tmp,idx, tmp[:idx], tmp[idx+1:])
            print(res)
            answer.append(int(res, 2))
    return answer


numbers = [2, 7]
result = [3, 11]

print(solution(numbers))